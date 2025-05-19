from rest_framework import serializers
from .models import Quiz, Question, Choice, QuizAttempt, Answer


class ChoiceSerializer(serializers.ModelSerializer):
    """Serializer for choice objects"""
    
    class Meta:
        model = Choice
        fields = ['id', 'text', 'is_correct']
        extra_kwargs = {
            'is_correct': {'write_only': True}  # Hide correct answer in list views
        }


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer for question objects"""
    choices = ChoiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'text', 'explanation', 'order', 'choices']


class QuizListSerializer(serializers.ModelSerializer):
    """Serializer for listing quiz objects"""
    question_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'subject', 'difficulty', 
                  'created_at', 'question_count', 'time_limit']
    
    def get_question_count(self, obj):
        return obj.questions.count()


class QuizDetailSerializer(serializers.ModelSerializer):
    """Serializer for detailed quiz objects"""
    questions = QuestionSerializer(many=True, read_only=True)
    question_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'subject', 'difficulty', 
                  'created_at', 'updated_at', 'questions', 'question_count', 'time_limit']
    
    def get_question_count(self, obj):
        return obj.questions.count()


class AnswerSerializer(serializers.ModelSerializer):
    """Serializer for answer objects"""
    question_text = serializers.CharField(source='question.text', read_only=True)
    selected_choice_text = serializers.SerializerMethodField()
    correct_choices = serializers.SerializerMethodField()
    is_correct = serializers.BooleanField(read_only=True)
    is_multiple_choice = serializers.BooleanField(source='question.is_multiple_choice', read_only=True)
    selected_choices_ids = serializers.PrimaryKeyRelatedField(
        source='selected_choices', many=True, read_only=True
    )
    
    class Meta:
        model = Answer
        fields = ['id', 'question', 'question_text', 'selected_choice', 'selected_choices_ids',
                  'selected_choice_text', 'correct_choices', 'is_correct', 'ai_explanation',
                  'is_multiple_choice']
        extra_kwargs = {
            'question': {'write_only': True},
            'selected_choice': {'write_only': True},
        }
    
    def get_selected_choice_text(self, obj):
        # Pour les questions à choix unique
        if not obj.question.is_multiple_choice and obj.selected_choice:
            return obj.selected_choice.text
        # Pour les questions à choix multiples
        elif obj.question.is_multiple_choice:
            return [choice.text for choice in obj.selected_choices.all()]
        return None
    
    def get_correct_choices(self, obj):
        # Only return the correct choices after the quiz is completed
        if obj.attempt.is_completed:
            if not obj.question.is_multiple_choice:
                correct_choice = obj.question.choices.filter(is_correct=True).first()
                if correct_choice:
                    return [correct_choice.text]
            else:
                correct_choices = obj.question.choices.filter(is_correct=True)
                return [choice.text for choice in correct_choices]
        return None


class QuizAttemptSerializer(serializers.ModelSerializer):
    """Serializer for quiz attempt objects"""
    answers = AnswerSerializer(many=True, read_only=True)
    quiz_title = serializers.CharField(source='quiz.title', read_only=True)
    
    class Meta:
        model = QuizAttempt
        fields = ['id', 'quiz', 'quiz_title', 'started_at', 'completed_at', 
                  'score', 'is_completed', 'answers']
        extra_kwargs = {
            'quiz': {'write_only': True},
        }


class SubmitAnswerSerializer(serializers.Serializer):
    """Serializer for submitting an answer"""
    question_id = serializers.IntegerField()
    choice_id = serializers.IntegerField(required=False)
    choice_ids = serializers.ListField(child=serializers.IntegerField(), required=False)
    
    def validate_question_id(self, value):
        try:
            question = Question.objects.get(id=value)
            return value
        except Question.DoesNotExist:
            raise serializers.ValidationError("Question does not exist")
    
    def validate(self, data):
        # Vérifier que nous avons soit choice_id soit choice_ids
        if 'choice_id' not in data and 'choice_ids' not in data:
            raise serializers.ValidationError("Either choice_id or choice_ids must be provided")
        
        # Récupérer la question
        try:
            question = Question.objects.get(id=data['question_id'])
        except Question.DoesNotExist:
            raise serializers.ValidationError("Question does not exist")
        
        # Pour les questions à choix unique, on doit avoir choice_id
        if not question.is_multiple_choice:
            if 'choice_id' not in data:
                raise serializers.ValidationError("choice_id is required for single choice questions")
            
            try:
                choice = Choice.objects.get(id=data['choice_id'])
                if choice.question.id != question.id:
                    raise serializers.ValidationError("Choice does not belong to the question")
            except Choice.DoesNotExist:
                raise serializers.ValidationError("Choice does not exist")
        
        # Pour les questions à choix multiples, on doit avoir choice_ids
        else:
            if 'choice_ids' not in data or not data['choice_ids']:
                raise serializers.ValidationError("choice_ids is required for multiple choice questions")
            
            # Vérifier que tous les choix appartiennent à la question
            for choice_id in data['choice_ids']:
                try:
                    choice = Choice.objects.get(id=choice_id)
                    if choice.question.id != question.id:
                        raise serializers.ValidationError(f"Choice {choice_id} does not belong to the question")
                except Choice.DoesNotExist:
                    raise serializers.ValidationError(f"Choice {choice_id} does not exist")
        
        return data
