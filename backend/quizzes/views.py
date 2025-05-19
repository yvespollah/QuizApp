from django.utils import timezone
from django.db.models import Count, Q
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Quiz, Question, Choice, QuizAttempt, Answer
from .serializers import (
    QuizListSerializer, QuizDetailSerializer, QuestionSerializer,
    QuizAttemptSerializer, AnswerSerializer, SubmitAnswerSerializer
)
from .ai_service import explanation_service


class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing quizzes"""
    queryset = Quiz.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuizDetailSerializer
        return QuizListSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filter by subject if provided
        subject = self.request.query_params.get('subject')
        if subject:
            queryset = queryset.filter(subject__icontains=subject)
        
        # Filter by difficulty if provided
        difficulty = self.request.query_params.get('difficulty')
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)
        
        return queryset
    
    @action(detail=True, methods=['post'])
    def start(self, request, pk=None):
        """Start a new quiz attempt"""
        quiz = self.get_object()
        
        # Check if there's an incomplete attempt
        existing_attempt = QuizAttempt.objects.filter(
            user=request.user,
            quiz=quiz,
            completed_at__isnull=True
        ).first()
        
        if existing_attempt:
            serializer = QuizAttemptSerializer(existing_attempt)
            return Response(serializer.data)
        
        # Create a new attempt
        attempt = QuizAttempt.objects.create(
            user=request.user,
            quiz=quiz
        )
        
        serializer = QuizAttemptSerializer(attempt)
        return Response(serializer.data)


class QuizAttemptViewSet(viewsets.ModelViewSet):
    """ViewSet for managing quiz attempts"""
    serializer_class = QuizAttemptSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return QuizAttempt.objects.filter(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def submit_answer(self, request, pk=None):
        """Submit an answer for a question in the quiz attempt"""
        attempt = self.get_object()
        
        # Ensure the attempt is not completed
        if attempt.is_completed:
            return Response(
                {"detail": "This quiz attempt has already been completed."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Validate the answer submission
        serializer = SubmitAnswerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        question_id = serializer.validated_data['question_id']
        
        # Get the question
        try:
            question = Question.objects.get(id=question_id, quiz=attempt.quiz)
        except Question.DoesNotExist:
            return Response(
                {"detail": "Invalid question."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if an answer already exists for this question
        existing_answer = Answer.objects.filter(attempt=attempt, question=question).first()
        
        # Traitement différent selon le type de question
        if question.is_multiple_choice:
            # Question à choix multiples
            choice_ids = serializer.validated_data.get('choice_ids', [])
            
            # Vérifier que tous les choix existent et appartiennent à la question
            choices = []
            for choice_id in choice_ids:
                try:
                    choice = Choice.objects.get(id=choice_id, question=question)
                    choices.append(choice)
                except Choice.DoesNotExist:
                    return Response(
                        {"detail": f"Invalid choice ID: {choice_id}."},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            
            if existing_answer:
                # Mettre à jour la réponse existante
                existing_answer.selected_choices.clear()  # Supprimer les choix précédents
                existing_answer.selected_choices.add(*choices)  # Ajouter les nouveaux choix
                answer = existing_answer
            else:
                # Créer une nouvelle réponse
                answer = Answer.objects.create(
                    attempt=attempt,
                    question=question
                )
                answer.selected_choices.set(choices)
        else:
            # Question à choix unique
            choice_id = serializer.validated_data.get('choice_id')
            
            try:
                choice = Choice.objects.get(id=choice_id, question=question)
            except Choice.DoesNotExist:
                return Response(
                    {"detail": "Invalid choice."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            if existing_answer:
                # Mettre à jour la réponse existante
                existing_answer.selected_choice = choice
                existing_answer.save()
                answer = existing_answer
            else:
                # Créer une nouvelle réponse
                answer = Answer.objects.create(
                    attempt=attempt,
                    question=question,
                    selected_choice=choice
                )
        
        return Response(AnswerSerializer(answer).data)
    
    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        """Complete a quiz attempt and generate AI explanations"""
        attempt = self.get_object()
        
        # Ensure the attempt is not already completed
        if attempt.is_completed:
            return Response(
                {"detail": "This quiz attempt has already been completed."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Mark the attempt as completed
        attempt.completed_at = timezone.now()
        
        # Calculate the score
        total_questions = attempt.quiz.questions.count()
        correct_answers = 0
        
        if total_questions > 0:
            # Récupérer toutes les réponses de cette tentative
            answers = Answer.objects.filter(attempt=attempt)
            
            for answer in answers:
                if answer.question.is_multiple_choice:
                    # Pour les questions à choix multiples
                    selected_choices = answer.selected_choices.all()
                    correct_choices = answer.question.choices.filter(is_correct=True)
                    
                    # Vérifier si toutes les réponses correctes ont été sélectionnées et aucune incorrecte
                    selected_ids = set(choice.id for choice in selected_choices)
                    correct_ids = set(choice.id for choice in correct_choices)
                    
                    if selected_ids == correct_ids:
                        correct_answers += 1
                else:
                    # Pour les questions à choix unique
                    if answer.selected_choice and answer.selected_choice.is_correct:
                        correct_answers += 1
            
            attempt.score = (correct_answers / total_questions) * 100
        else:
            attempt.score = 0
        
        attempt.save()
        
        # Generate AI explanations for each answer
        answers = Answer.objects.filter(attempt=attempt)
        for answer in answers:
            question_text = answer.question.text
            
            if answer.question.is_multiple_choice:
                # Pour les questions à choix multiples
                correct_choices = answer.question.choices.filter(is_correct=True)
                correct_answer_text = ", ".join([choice.text for choice in correct_choices])
                
                selected_choices = answer.selected_choices.all()
                user_answer_text = ", ".join([choice.text for choice in selected_choices])
                
                # Vérifier si la réponse est correcte
                selected_ids = set(choice.id for choice in selected_choices)
                correct_ids = set(choice.id for choice in correct_choices)
                is_correct = selected_ids == correct_ids
            else:
                # Pour les questions à choix unique
                correct_choice = answer.question.choices.filter(is_correct=True).first()
                correct_answer_text = correct_choice.text if correct_choice else "Unknown"
                user_answer_text = answer.selected_choice.text if answer.selected_choice else "No answer"
                is_correct = answer.selected_choice and answer.selected_choice.is_correct
            
            # Generate AI explanation
            explanation = explanation_service.generate_explanation(
                question_text, correct_answer_text, user_answer_text, is_correct
            )
            
            # If there's a manual explanation, use it instead
            if answer.question.explanation:
                explanation = answer.question.explanation
            
            answer.ai_explanation = explanation
            answer.save()
        
        serializer = QuizAttemptSerializer(attempt)
        return Response(serializer.data)


class UserQuizHistoryView(generics.ListAPIView):
    """View for listing a user's quiz history"""
    serializer_class = QuizAttemptSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return QuizAttempt.objects.filter(
            user=self.request.user,
            completed_at__isnull=False
        ).order_by('-completed_at')
