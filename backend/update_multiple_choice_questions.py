#!/usr/bin/env python
import os
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quizzes.models import Question, Choice

def update_multiple_choice_questions():
    """
    Identifie et met à jour les questions à choix multiples.
    Une question est considérée comme à choix multiples si elle a plusieurs réponses correctes.
    """
    # Récupérer toutes les questions
    all_questions = Question.objects.all()
    
    updated_count = 0
    
    for question in all_questions:
        # Compter le nombre de réponses correctes
        correct_choices_count = question.choices.filter(is_correct=True).count()
        
        # Si plus d'une réponse correcte, c'est une question à choix multiples
        is_multiple = correct_choices_count > 1
        
        # Mettre à jour la question si nécessaire
        if question.is_multiple_choice != is_multiple:
            question.is_multiple_choice = is_multiple
            question.save()
            updated_count += 1
            print(f"Question ID {question.id} mise à jour: is_multiple_choice = {is_multiple}")
    
    print(f"\nMise à jour terminée. {updated_count} questions ont été mises à jour.")

if __name__ == "__main__":
    update_multiple_choice_questions()
