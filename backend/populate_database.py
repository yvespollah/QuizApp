import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quizzes.models import Quiz, Question, Choice
from django.contrib.auth import get_user_model

User = get_user_model()

# Données pour les quiz
QUIZ_DATA = [
    {
        'title': 'Introduction à Python',
        'description': 'Un quiz pour tester vos connaissances de base en Python.',
        'subject': 'Programmation',
        'difficulty': 'easy',
        'time_limit': 15,
        'questions': [
            {
                'text': 'Quelle est la syntaxe correcte pour afficher "Hello World" en Python ?',
                'explanation': 'La fonction print() est utilisée pour afficher du texte en Python.',
                'choices': [
                    {'text': 'print("Hello World")', 'is_correct': True},
                    {'text': 'echo("Hello World")', 'is_correct': False},
                    {'text': 'console.log("Hello World")', 'is_correct': False},
                    {'text': 'System.out.println("Hello World")', 'is_correct': False},
                ]
            },
            {
                'text': 'Comment déclarer une liste vide en Python ?',
                'explanation': 'Une liste vide peut être déclarée avec des crochets vides [].',
                'choices': [
                    {'text': 'list = []', 'is_correct': True},
                    {'text': 'list = {}', 'is_correct': False},
                    {'text': 'list = ()', 'is_correct': False},
                    {'text': 'list = new List()', 'is_correct': False},
                ]
            },
            {
                'text': 'Quel est le résultat de 3 ** 2 en Python ?',
                'explanation': 'L\'opérateur ** est utilisé pour l\'exponentiation en Python. 3 ** 2 signifie 3 au carré, soit 9.',
                'choices': [
                    {'text': '9', 'is_correct': True},
                    {'text': '6', 'is_correct': False},
                    {'text': '5', 'is_correct': False},
                    {'text': '8', 'is_correct': False},
                ]
            },
            {
                'text': 'Comment accéder au premier élément d\'une liste nommée "fruits" ?',
                'explanation': 'En Python, l\'indexation commence à 0, donc le premier élément est à l\'index 0.',
                'choices': [
                    {'text': 'fruits[0]', 'is_correct': True},
                    {'text': 'fruits[1]', 'is_correct': False},
                    {'text': 'fruits(0)', 'is_correct': False},
                    {'text': 'fruits.first()', 'is_correct': False},
                ]
            },
            {
                'text': 'Quelle est la méthode pour ajouter un élément à la fin d\'une liste ?',
                'explanation': 'La méthode append() ajoute un élément à la fin d\'une liste.',
                'choices': [
                    {'text': 'append()', 'is_correct': True},
                    {'text': 'add()', 'is_correct': False},
                    {'text': 'insert()', 'is_correct': False},
                    {'text': 'push()', 'is_correct': False},
                ]
            },
        ]
    },
    {
        'title': 'HTML et CSS Fondamentaux',
        'description': 'Testez vos connaissances sur les bases du HTML et CSS.',
        'subject': 'Développement Web',
        'difficulty': 'medium',
        'time_limit': 20,
        'questions': [
            {
                'text': 'Quelle balise HTML est utilisée pour créer un lien hypertexte ?',
                'explanation': 'La balise <a> est utilisée pour créer des liens hypertextes en HTML.',
                'choices': [
                    {'text': '<a>', 'is_correct': True},
                    {'text': '<link>', 'is_correct': False},
                    {'text': '<href>', 'is_correct': False},
                    {'text': '<url>', 'is_correct': False},
                ]
            },
            {
                'text': 'Comment définir la couleur de fond d\'un élément en CSS ?',
                'explanation': 'La propriété background-color est utilisée pour définir la couleur de fond d\'un élément.',
                'choices': [
                    {'text': 'background-color', 'is_correct': True},
                    {'text': 'color-background', 'is_correct': False},
                    {'text': 'bgcolor', 'is_correct': False},
                    {'text': 'color', 'is_correct': False},
                ]
            },
            {
                'text': 'Quelle balise HTML est utilisée pour créer un titre de niveau 1 ?',
                'explanation': 'La balise <h1> est utilisée pour créer un titre de niveau 1 (le plus important).',
                'choices': [
                    {'text': '<h1>', 'is_correct': True},
                    {'text': '<heading>', 'is_correct': False},
                    {'text': '<title>', 'is_correct': False},
                    {'text': '<header>', 'is_correct': False},
                ]
            },
            {
                'text': 'Comment sélectionner tous les éléments de classe "btn" en CSS ?',
                'explanation': 'Le sélecteur de classe en CSS est un point (.) suivi du nom de la classe.',
                'choices': [
                    {'text': '.btn', 'is_correct': True},
                    {'text': '#btn', 'is_correct': False},
                    {'text': 'btn', 'is_correct': False},
                    {'text': '*btn', 'is_correct': False},
                ]
            },
            {
                'text': 'Quelle propriété CSS est utilisée pour changer la taille du texte ?',
                'explanation': 'La propriété font-size est utilisée pour définir la taille du texte.',
                'choices': [
                    {'text': 'font-size', 'is_correct': True},
                    {'text': 'text-size', 'is_correct': False},
                    {'text': 'text-style', 'is_correct': False},
                    {'text': 'font-height', 'is_correct': False},
                ]
            },
        ]
    },
    {
        'title': 'JavaScript Avancé',
        'description': 'Un quiz pour tester vos connaissances avancées en JavaScript.',
        'subject': 'Programmation',
        'difficulty': 'hard',
        'time_limit': 30,
        'questions': [
            {
                'text': 'Qu\'est-ce qu\'une closure en JavaScript ?',
                'explanation': 'Une closure est une fonction qui a accès aux variables de sa fonction parente, même après que celle-ci ait terminé son exécution.',
                'choices': [
                    {'text': 'Une fonction qui a accès aux variables de sa fonction parente', 'is_correct': True},
                    {'text': 'Une méthode pour fermer une connexion', 'is_correct': False},
                    {'text': 'Un objet qui encapsule des données', 'is_correct': False},
                    {'text': 'Une fonction qui ne retourne rien', 'is_correct': False},
                ]
            },
            {
                'text': 'Quelle méthode est utilisée pour créer une promesse en JavaScript ?',
                'explanation': 'Le constructeur Promise est utilisé pour créer une nouvelle promesse en JavaScript.',
                'choices': [
                    {'text': 'new Promise()', 'is_correct': True},
                    {'text': 'Promise.create()', 'is_correct': False},
                    {'text': 'async()', 'is_correct': False},
                    {'text': 'await()', 'is_correct': False},
                ]
            },
            {
                'text': 'Comment déclarer une fonction fléchée (arrow function) en JavaScript ?',
                'explanation': 'Les fonctions fléchées sont déclarées avec la syntaxe () => {}.',
                'choices': [
                    {'text': '() => {}', 'is_correct': True},
                    {'text': 'function() => {}', 'is_correct': False},
                    {'text': '=> function() {}', 'is_correct': False},
                    {'text': 'function arrow() {}', 'is_correct': False},
                ]
            },
            {
                'text': 'Quel est le résultat de typeof null en JavaScript ?',
                'explanation': 'En JavaScript, typeof null retourne "object", ce qui est considéré comme un bug historique du langage.',
                'choices': [
                    {'text': '"object"', 'is_correct': True},
                    {'text': '"null"', 'is_correct': False},
                    {'text': '"undefined"', 'is_correct': False},
                    {'text': '"string"', 'is_correct': False},
                ]
            },
            {
                'text': 'Comment créer un nouvel objet en JavaScript ?',
                'explanation': 'Il existe plusieurs façons de créer un objet en JavaScript, mais la plus courante est d\'utiliser la notation littérale d\'objet {}.',
                'choices': [
                    {'text': '{}', 'is_correct': True},
                    {'text': 'Object.create()', 'is_correct': False},
                    {'text': 'new Object()', 'is_correct': False},
                    {'text': 'Toutes les réponses sont correctes', 'is_correct': False},
                ]
            },
        ]
    },
    {
        'title': 'Bases de données SQL',
        'description': 'Testez vos connaissances sur les bases de données SQL.',
        'subject': 'Bases de données',
        'difficulty': 'medium',
        'time_limit': 25,
        'questions': [
            {
                'text': 'Quelle commande SQL est utilisée pour récupérer des données d\'une table ?',
                'explanation': 'La commande SELECT est utilisée pour récupérer des données d\'une ou plusieurs tables.',
                'choices': [
                    {'text': 'SELECT', 'is_correct': True},
                    {'text': 'GET', 'is_correct': False},
                    {'text': 'EXTRACT', 'is_correct': False},
                    {'text': 'QUERY', 'is_correct': False},
                ]
            },
            {
                'text': 'Quelle clause SQL est utilisée pour filtrer les résultats ?',
                'explanation': 'La clause WHERE est utilisée pour filtrer les résultats d\'une requête SQL.',
                'choices': [
                    {'text': 'WHERE', 'is_correct': True},
                    {'text': 'FILTER', 'is_correct': False},
                    {'text': 'HAVING', 'is_correct': False},
                    {'text': 'CONDITION', 'is_correct': False},
                ]
            },
            {
                'text': 'Comment joindre deux tables en SQL ?',
                'explanation': 'La clause JOIN est utilisée pour combiner des lignes de deux ou plusieurs tables.',
                'choices': [
                    {'text': 'JOIN', 'is_correct': True},
                    {'text': 'MERGE', 'is_correct': False},
                    {'text': 'COMBINE', 'is_correct': False},
                    {'text': 'CONNECT', 'is_correct': False},
                ]
            },
            {
                'text': 'Quelle commande SQL est utilisée pour ajouter des données à une table ?',
                'explanation': 'La commande INSERT est utilisée pour ajouter de nouvelles lignes à une table.',
                'choices': [
                    {'text': 'INSERT', 'is_correct': True},
                    {'text': 'ADD', 'is_correct': False},
                    {'text': 'UPDATE', 'is_correct': False},
                    {'text': 'CREATE', 'is_correct': False},
                ]
            },
            {
                'text': 'Quelle fonction SQL retourne le nombre de lignes dans un résultat ?',
                'explanation': 'La fonction COUNT() retourne le nombre de lignes qui correspondent à un critère spécifié.',
                'choices': [
                    {'text': 'COUNT()', 'is_correct': True},
                    {'text': 'SUM()', 'is_correct': False},
                    {'text': 'TOTAL()', 'is_correct': False},
                    {'text': 'NUM()', 'is_correct': False},
                ]
            },
        ]
    },
    {
        'title': 'Réseaux Informatiques',
        'description': 'Un quiz pour tester vos connaissances sur les réseaux informatiques.',
        'subject': 'Informatique',
        'difficulty': 'hard',
        'time_limit': 30,
        'questions': [
            {
                'text': 'Quel protocole est utilisé pour envoyer des emails ?',
                'explanation': 'SMTP (Simple Mail Transfer Protocol) est le protocole standard pour l\'envoi d\'emails.',
                'choices': [
                    {'text': 'SMTP', 'is_correct': True},
                    {'text': 'HTTP', 'is_correct': False},
                    {'text': 'FTP', 'is_correct': False},
                    {'text': 'SSH', 'is_correct': False},
                ]
            },
            {
                'text': 'Quelle est la plage d\'adresses IP privées de classe C ?',
                'explanation': 'La plage d\'adresses IP privées de classe C est 192.168.0.0 à 192.168.255.255.',
                'choices': [
                    {'text': '192.168.0.0 - 192.168.255.255', 'is_correct': True},
                    {'text': '10.0.0.0 - 10.255.255.255', 'is_correct': False},
                    {'text': '172.16.0.0 - 172.31.255.255', 'is_correct': False},
                    {'text': '127.0.0.0 - 127.255.255.255', 'is_correct': False},
                ]
            },
            {
                'text': 'Quel est le port par défaut pour HTTPS ?',
                'explanation': 'Le port par défaut pour HTTPS (HTTP Secure) est 443.',
                'choices': [
                    {'text': '443', 'is_correct': True},
                    {'text': '80', 'is_correct': False},
                    {'text': '8080', 'is_correct': False},
                    {'text': '22', 'is_correct': False},
                ]
            },
            {
                'text': 'Quelle couche du modèle OSI est responsable du routage ?',
                'explanation': 'La couche réseau (couche 3) du modèle OSI est responsable du routage des paquets.',
                'choices': [
                    {'text': 'Couche 3 (Réseau)', 'is_correct': True},
                    {'text': 'Couche 2 (Liaison de données)', 'is_correct': False},
                    {'text': 'Couche 4 (Transport)', 'is_correct': False},
                    {'text': 'Couche 1 (Physique)', 'is_correct': False},
                ]
            },
            {
                'text': 'Quel protocole est utilisé pour résoudre les adresses IP en adresses MAC ?',
                'explanation': 'ARP (Address Resolution Protocol) est utilisé pour résoudre les adresses IP en adresses MAC.',
                'choices': [
                    {'text': 'ARP', 'is_correct': True},
                    {'text': 'DNS', 'is_correct': False},
                    {'text': 'DHCP', 'is_correct': False},
                    {'text': 'ICMP', 'is_correct': False},
                ]
            },
        ]
    }
]

def populate_database():
    print("Suppression des données existantes...")
    Quiz.objects.all().delete()
    
    print("Création des quiz...")
    for quiz_data in QUIZ_DATA:
        # Créer le quiz
        quiz = Quiz.objects.create(
            title=quiz_data['title'],
            description=quiz_data['description'],
            subject=quiz_data['subject'],
            difficulty=quiz_data['difficulty'],
            time_limit=quiz_data['time_limit']
        )
        
        # Créer les questions et les choix
        for i, question_data in enumerate(quiz_data['questions']):
            question = Question.objects.create(
                quiz=quiz,
                text=question_data['text'],
                explanation=question_data['explanation'],
                order=i
            )
            
            for choice_data in question_data['choices']:
                Choice.objects.create(
                    question=question,
                    text=choice_data['text'],
                    is_correct=choice_data['is_correct']
                )
        
        print(f"Quiz '{quiz.title}' créé avec {len(quiz_data['questions'])} questions.")
    
    print("Base de données remplie avec succès!")

if __name__ == "__main__":
    populate_database()
