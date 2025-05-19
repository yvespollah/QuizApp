from django.db import models
from django.conf import settings


class Quiz(models.Model):
    """Model representing a quiz"""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    subject = models.CharField(max_length=100)
    difficulty = models.CharField(
        max_length=20,
        choices=[
            ('easy', 'Easy'),
            ('medium', 'Medium'),
            ('hard', 'Hard'),
        ],
        default='medium'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    time_limit = models.IntegerField(help_text="Time limit in minutes", null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    @property
    def question_count(self):
        return self.questions.count()


class Question(models.Model):
    """Model representing a question in a quiz"""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    explanation = models.TextField(blank=True, help_text="Manual explanation for this question")
    order = models.IntegerField(default=0)
    is_multiple_choice = models.BooleanField(default=False, help_text="Whether multiple answers can be selected")
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.quiz.title} - Question {self.order}"


class Choice(models.Model):
    """Model representing a choice for a question"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text


class QuizAttempt(models.Model):
    """Model representing a user's attempt at a quiz"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quiz_attempts')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempts')
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}"
    
    @property
    def is_completed(self):
        return self.completed_at is not None


class Answer(models.Model):
    """Model representing a user's answer to a question"""
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    selected_choices = models.ManyToManyField(Choice, related_name='selected_in_answers', blank=True)
    ai_explanation = models.TextField(blank=True, help_text="AI-generated explanation for this answer")
    
    def __str__(self):
        return f"{self.attempt.user.username} - {self.question.text[:30]}"
    
    @property
    def is_correct(self):
        # Pour les questions à choix unique
        if not self.question.is_multiple_choice and self.selected_choice:
            return self.selected_choice.is_correct
        
        # Pour les questions à choix multiples
        elif self.question.is_multiple_choice:
            # Récupérer tous les choix corrects pour cette question
            correct_choices = set(self.question.choices.filter(is_correct=True).values_list('id', flat=True))
            # Récupérer tous les choix sélectionnés par l'utilisateur
            selected = set(self.selected_choices.values_list('id', flat=True))
            
            # La réponse est correcte si l'utilisateur a sélectionné exactement tous les choix corrects
            return correct_choices == selected
        
        return False
