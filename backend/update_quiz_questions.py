#!/usr/bin/env python
import os
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quizzes.models import Quiz, Question, Choice

def update_multiple_choice_questions():
    """
    Met à jour les questions existantes pour définir correctement le champ is_multiple_choice.
    Une question est considérée à choix multiples si elle a plusieurs réponses correctes.
    """
    # Récupérer toutes les questions
    questions = Question.objects.all()
    
    # Compteurs pour les statistiques
    single_choice_count = 0
    multiple_choice_count = 0
    
    for question in questions:
        # Compter le nombre de réponses correctes
        correct_choices_count = question.choices.filter(is_correct=True).count()
        
        # Si la question a plus d'une réponse correcte, c'est une question à choix multiples
        if correct_choices_count > 1:
            question.is_multiple_choice = True
            multiple_choice_count += 1
        else:
            question.is_multiple_choice = False
            single_choice_count += 1
        
        question.save()
    
    return single_choice_count, multiple_choice_count

if __name__ == "__main__":
    print("Mise à jour des questions existantes...")
    single_count, multiple_count = update_multiple_choice_questions()
    print(f"Mise à jour terminée. {single_count} questions à choix unique et {multiple_count} questions à choix multiples.")
