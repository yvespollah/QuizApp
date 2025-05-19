#!/usr/bin/env python
import os
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quizzes.models import Quiz, Question, Choice

# Création du quiz
quiz = Quiz.objects.create(
    title="C Programming Language",
    description="Test your knowledge of the C programming language with questions covering basic syntax, memory management, pointers, and more.",
    subject="Programming",
    difficulty="medium",
    time_limit=30  # 30 minutes
)

print(f"Quiz créé: {quiz.title}")

# Questions à choix unique
single_choice_questions = [
    {
        "text": "Which of the following is the correct way to declare a pointer to an integer in C?",
        "choices": [
            {"text": "int ptr;", "is_correct": False},
            {"text": "int *ptr;", "is_correct": True},
            {"text": "int &ptr;", "is_correct": False},
            {"text": "pointer int ptr;", "is_correct": False}
        ]
    },
    {
        "text": "What is the output of the following code?\n\nint x = 5;\nprintf(\"%d\", x++);",
        "choices": [
            {"text": "5", "is_correct": True},
            {"text": "6", "is_correct": False},
            {"text": "4", "is_correct": False},
            {"text": "Compilation error", "is_correct": False}
        ]
    },
    {
        "text": "Which function is used to allocate memory dynamically in C?",
        "choices": [
            {"text": "alloc()", "is_correct": False},
            {"text": "malloc()", "is_correct": True},
            {"text": "realloc()", "is_correct": False},
            {"text": "dealloc()", "is_correct": False}
        ]
    },
    {
        "text": "What is the size of an int data type in C (on most 32-bit systems)?",
        "choices": [
            {"text": "1 byte", "is_correct": False},
            {"text": "2 bytes", "is_correct": False},
            {"text": "4 bytes", "is_correct": True},
            {"text": "8 bytes", "is_correct": False}
        ]
    },
    {
        "text": "Which operator is used to access the value at an address stored in a pointer?",
        "choices": [
            {"text": "&", "is_correct": False},
            {"text": "*", "is_correct": True},
            {"text": "->", "is_correct": False},
            {"text": "#", "is_correct": False}
        ]
    },
    {
        "text": "What does the 'static' keyword do when used with a local variable?",
        "choices": [
            {"text": "Makes the variable accessible across files", "is_correct": False},
            {"text": "Makes the variable retain its value between function calls", "is_correct": True},
            {"text": "Makes the variable read-only", "is_correct": False},
            {"text": "Makes the variable thread-safe", "is_correct": False}
        ]
    },
    {
        "text": "Which of the following is NOT a valid C data type?",
        "choices": [
            {"text": "int", "is_correct": False},
            {"text": "float", "is_correct": False},
            {"text": "string", "is_correct": True},
            {"text": "char", "is_correct": False}
        ]
    },
    {
        "text": "What is the correct way to access the third element of an array named 'arr'?",
        "choices": [
            {"text": "arr[3]", "is_correct": False},
            {"text": "arr[2]", "is_correct": True},
            {"text": "arr(2)", "is_correct": False},
            {"text": "arr.3", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of the 'break' statement in a switch case?",
        "choices": [
            {"text": "To exit the program", "is_correct": False},
            {"text": "To skip the current iteration of a loop", "is_correct": False},
            {"text": "To terminate the switch statement", "is_correct": True},
            {"text": "To return a value from a function", "is_correct": False}
        ]
    },
    {
        "text": "Which header file should be included to use the printf() function?",
        "choices": [
            {"text": "<stdlib.h>", "is_correct": False},
            {"text": "<math.h>", "is_correct": False},
            {"text": "<stdio.h>", "is_correct": True},
            {"text": "<string.h>", "is_correct": False}
        ]
    }
]

# Questions à choix multiples
multiple_choice_questions = [
    {
        "text": "Which of the following are valid ways to comment code in C?",
        "choices": [
            {"text": "// Single line comment", "is_correct": True},
            {"text": "/* Multi-line comment */", "is_correct": True},
            {"text": "# Comment", "is_correct": False},
            {"text": "<!-- Comment -->", "is_correct": False}
        ]
    },
    {
        "text": "Which of the following functions are used for dynamic memory allocation in C?",
        "choices": [
            {"text": "malloc()", "is_correct": True},
            {"text": "calloc()", "is_correct": True},
            {"text": "realloc()", "is_correct": True},
            {"text": "alloc()", "is_correct": False}
        ]
    },
    {
        "text": "Which of the following are valid escape sequences in C?",
        "choices": [
            {"text": "\\n", "is_correct": True},
            {"text": "\\t", "is_correct": True},
            {"text": "\\v", "is_correct": True},
            {"text": "\\p", "is_correct": False}
        ]
    },
    {
        "text": "Which of the following are valid storage class specifiers in C?",
        "choices": [
            {"text": "auto", "is_correct": True},
            {"text": "register", "is_correct": True},
            {"text": "static", "is_correct": True},
            {"text": "dynamic", "is_correct": False}
        ]
    },
    {
        "text": "Which of the following are valid bitwise operators in C?",
        "choices": [
            {"text": "&", "is_correct": True},
            {"text": "|", "is_correct": True},
            {"text": "^", "is_correct": True},
            {"text": "?", "is_correct": False}
        ]
    },
    {
        "text": "Which of the following statements about pointers in C are true?",
        "choices": [
            {"text": "Pointers store memory addresses", "is_correct": True},
            {"text": "Pointers can be used to implement pass-by-reference", "is_correct": True},
            {"text": "Pointers are always 4 bytes in size", "is_correct": False},
            {"text": "Pointers can be used for dynamic memory allocation", "is_correct": True}
        ]
    },
    {
        "text": "Which of the following are valid preprocessor directives in C?",
        "choices": [
            {"text": "#include", "is_correct": True},
            {"text": "#define", "is_correct": True},
            {"text": "#ifdef", "is_correct": True},
            {"text": "#import", "is_correct": False}
        ]
    },
    {
        "text": "Which of the following are valid ways to declare and initialize an array in C?",
        "choices": [
            {"text": "int arr[5] = {1, 2, 3, 4, 5};", "is_correct": True},
            {"text": "int arr[] = {1, 2, 3, 4, 5};", "is_correct": True},
            {"text": "int arr[5]; arr = {1, 2, 3, 4, 5};", "is_correct": False},
            {"text": "int arr[5] = 1, 2, 3, 4, 5;", "is_correct": False}
        ]
    },
    {
        "text": "Which of the following functions are used for file handling in C?",
        "choices": [
            {"text": "fopen()", "is_correct": True},
            {"text": "fclose()", "is_correct": True},
            {"text": "fread()", "is_correct": True},
            {"text": "fstart()", "is_correct": False}
        ]
    },
    {
        "text": "Which of the following are valid loop constructs in C?",
        "choices": [
            {"text": "for", "is_correct": True},
            {"text": "while", "is_correct": True},
            {"text": "do-while", "is_correct": True},
            {"text": "foreach", "is_correct": False}
        ]
    }
]

# Questions vrai/faux
true_false_questions = [
    {
        "text": "In C, arrays are passed to functions by value.",
        "choices": [
            {"text": "True", "is_correct": False},
            {"text": "False", "is_correct": True}
        ]
    },
    {
        "text": "The sizeof() operator returns the size of a variable in bits.",
        "choices": [
            {"text": "True", "is_correct": False},
            {"text": "False", "is_correct": True}
        ]
    },
    {
        "text": "In C, strings are terminated with a null character ('\\0').",
        "choices": [
            {"text": "True", "is_correct": True},
            {"text": "False", "is_correct": False}
        ]
    },
    {
        "text": "The 'const' keyword in C makes a variable completely immutable.",
        "choices": [
            {"text": "True", "is_correct": False},
            {"text": "False", "is_correct": True}
        ]
    },
    {
        "text": "C supports object-oriented programming natively.",
        "choices": [
            {"text": "True", "is_correct": False},
            {"text": "False", "is_correct": True}
        ]
    }
]

# Combiner toutes les questions
all_questions = []

# Ajouter les questions à choix unique
for q in single_choice_questions:
    q["is_multiple_choice"] = False
    all_questions.append(q)

# Ajouter les questions à choix multiples avec le flag is_multiple_choice=True
for q in multiple_choice_questions:
    q["is_multiple_choice"] = True
    all_questions.append(q)

# Ajouter les questions vrai/faux
for q in true_false_questions:
    q["is_multiple_choice"] = False
    all_questions.append(q)

# Ajouter toutes les questions au quiz
for i, q_data in enumerate(all_questions, 1):
    # Créer la question
    question = Question.objects.create(
        quiz=quiz,
        text=q_data["text"],
        is_multiple_choice=q_data["is_multiple_choice"]
    )
    
    # Ajouter les choix
    for c_data in q_data["choices"]:
        Choice.objects.create(
            question=question,
            text=c_data["text"],
            is_correct=c_data["is_correct"]
        )
    
    question_type = "choix unique"
    if q_data["is_multiple_choice"]:
        question_type = "choix multiples"
    elif len(q_data["choices"]) == 2:
        question_type = "choix unique"
    
    print(f"Question {i} ajoutée ({question_type}) avec {len(q_data['choices'])} choix")

# Résumé
single_count = len(single_choice_questions)
multiple_count = len(multiple_choice_questions)
tf_count = len(true_false_questions)

print(f"\nQuiz {quiz.title} créé avec succès avec {single_count} questions à choix unique, {multiple_count} questions à choix multiples, et {tf_count} questions vrai/faux.")
