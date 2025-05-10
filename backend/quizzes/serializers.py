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
    selected_choice_text = serializers.CharField(source='selected_choice.text', read_only=True)
    correct_choice = serializers.SerializerMethodField()
    is_correct = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Answer
        fields = ['id', 'question', 'question_text', 'selected_choice', 
                  'selected_choice_text', 'correct_choice', 'is_correct', 'ai_explanation']
        extra_kwargs = {
            'question': {'write_only': True},
            'selected_choice': {'write_only': True},
        }
    
    def get_correct_choice(self, obj):
        # Only return the correct choice after the quiz is completed
        if obj.attempt.is_completed:
            correct_choice = obj.question.choices.filter(is_correct=True).first()
            if correct_choice:
                return correct_choice.text
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
    choice_id = serializers.IntegerField()
    
    def validate_question_id(self, value):
        try:
            question = Question.objects.get(id=value)
            return value
        except Question.DoesNotExist:
            raise serializers.ValidationError("Question does not exist")
    
    def validate_choice_id(self, value):
        try:
            choice = Choice.objects.get(id=value)
            return value
        except Choice.DoesNotExist:
            raise serializers.ValidationError("Choice does not exist")
    
    def validate(self, data):
        question_id = data.get('question_id')
        choice_id = data.get('choice_id')
        
        # Ensure the choice belongs to the question
        try:
            question = Question.objects.get(id=question_id)
            choice = Choice.objects.get(id=choice_id)
            
            if choice.question.id != question.id:
                raise serializers.ValidationError(
                    {"choice_id": "This choice does not belong to the specified question"}
                )
        except (Question.DoesNotExist, Choice.DoesNotExist):
            pass  # Already validated in individual field validations
        
        return data
