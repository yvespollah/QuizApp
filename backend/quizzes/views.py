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
        choice_id = serializer.validated_data['choice_id']
        
        # Get the question and choice
        try:
            question = Question.objects.get(id=question_id, quiz=attempt.quiz)
            choice = Choice.objects.get(id=choice_id, question=question)
        except (Question.DoesNotExist, Choice.DoesNotExist):
            return Response(
                {"detail": "Invalid question or choice."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if an answer already exists for this question
        existing_answer = Answer.objects.filter(attempt=attempt, question=question).first()
        if existing_answer:
            existing_answer.selected_choice = choice
            existing_answer.save()
            answer = existing_answer
        else:
            # Create a new answer
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
        if total_questions > 0:
            correct_answers = Answer.objects.filter(
                attempt=attempt,
                selected_choice__is_correct=True
            ).count()
            attempt.score = (correct_answers / total_questions) * 100
        else:
            attempt.score = 0
        
        attempt.save()
        
        # Generate AI explanations for each answer
        answers = Answer.objects.filter(attempt=attempt)
        for answer in answers:
            question_text = answer.question.text
            correct_choice = answer.question.choices.filter(is_correct=True).first()
            correct_answer_text = correct_choice.text if correct_choice else "Unknown"
            user_answer_text = answer.selected_choice.text
            is_correct = answer.is_correct
            
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
