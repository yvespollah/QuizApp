#!/usr/bin/env python
import os
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quizzes.models import Quiz, Question, Choice

# Création du quiz
quiz = Quiz.objects.create(
    title="Huawei Device Commands and Configuration",
    description="25 practice questions covering Huawei device commands, configuration, and management concepts.",
    subject="Huawei HCIA",
    difficulty="medium",
    time_limit=20  # 20 minutes
)

print(f"Quiz créé: {quiz.title}")

# Questions à choix unique
single_choice_questions = [
    {
        "text": "What memory type stores the running system information on a Huawei device?",
        "choices": [
            {"text": "Flash memory", "is_correct": False},
            {"text": "NVRAM", "is_correct": False},
            {"text": "SDRAM", "is_correct": True},
            {"text": "BootROM", "is_correct": False}
        ]
    },
    {
        "text": "What is the first view displayed after logging into a Huawei device?",
        "choices": [
            {"text": "System view", "is_correct": False},
            {"text": "Interface view", "is_correct": False},
            {"text": "User view", "is_correct": True},
            {"text": "Configuration view", "is_correct": False}
        ]
    },
    {
        "text": "Which command is used to move a file within the same storage medium?",
        "choices": [
            {"text": "copy", "is_correct": False},
            {"text": "rename", "is_correct": True},
            {"text": "move", "is_correct": False},
            {"text": "delete", "is_correct": False}
        ]
    },
    {
        "text": "What is the maximum user level that can be assigned on Huawei devices?",
        "choices": [
            {"text": "3", "is_correct": False},
            {"text": "7", "is_correct": False},
            {"text": "10", "is_correct": False},
            {"text": "15", "is_correct": True}
        ]
    },
    {
        "text": "Which port is commonly used for local login to Huawei devices?",
        "choices": [
            {"text": "USB", "is_correct": False},
            {"text": "Console port", "is_correct": True},
            {"text": "VTY", "is_correct": False},
            {"text": "Ethernet", "is_correct": False}
        ]
    },
    {
        "text": "Which command enables you to configure the system clock of the device?",
        "choices": [
            {"text": "clock time", "is_correct": False},
            {"text": "set time", "is_correct": False},
            {"text": "clock datetime", "is_correct": True},
            {"text": "datetime set", "is_correct": False}
        ]
    },
    {
        "text": "Which of the following login methods is disabled by default and must be configured first?",
        "choices": [
            {"text": "Console", "is_correct": False},
            {"text": "FTP", "is_correct": False},
            {"text": "SSH", "is_correct": True},
            {"text": "Telnet", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of the system-view command?",
        "choices": [
            {"text": "Save the configuration", "is_correct": False},
            {"text": "Show startup file", "is_correct": False},
            {"text": "Enter global configuration mode", "is_correct": True},
            {"text": "Display user view", "is_correct": False}
        ]
    },
    {
        "text": "Which command displays information about the startup configuration and software?",
        "choices": [
            {"text": "display version", "is_correct": True},
            {"text": "display boot", "is_correct": False},
            {"text": "display startup", "is_correct": False},
            {"text": "show configuration", "is_correct": False}
        ]
    },
    {
        "text": "Which logical interface is typically used as a management interface?",
        "choices": [
            {"text": "VTY", "is_correct": False},
            {"text": "GE0/0/0", "is_correct": False},
            {"text": "Console", "is_correct": False},
            {"text": "Loopback", "is_correct": True}
        ]
    }
]

# Questions à choix multiples
multiple_choice_questions = [
    {
        "text": "Which storage media are nonvolatile?",
        "choices": [
            {"text": "Flash memory", "is_correct": True},
            {"text": "SDRAM", "is_correct": False},
            {"text": "SD card", "is_correct": True},
            {"text": "BootROM", "is_correct": True}
        ]
    },
    {
        "text": "Which of the following are valid login methods for a Huawei device?",
        "choices": [
            {"text": "Telnet", "is_correct": True},
            {"text": "SSH", "is_correct": True},
            {"text": "FTP", "is_correct": False},
            {"text": "Console", "is_correct": True}
        ]
    },
    {
        "text": "Which commands are related to file or directory manipulation?",
        "choices": [
            {"text": "mkdir", "is_correct": True},
            {"text": "rename", "is_correct": True},
            {"text": "shutdown", "is_correct": False},
            {"text": "cd", "is_correct": True}
        ]
    },
    {
        "text": "What can be viewed using the dir command?",
        "choices": [
            {"text": "Directory content", "is_correct": True},
            {"text": "File content", "is_correct": False},
            {"text": "Current path", "is_correct": False},
            {"text": "File list", "is_correct": True}
        ]
    },
    {
        "text": "Which commands are used to delete files?",
        "choices": [
            {"text": "delete", "is_correct": True},
            {"text": "reset recycle-bin", "is_correct": True},
            {"text": "copy", "is_correct": False},
            {"text": "rmdir", "is_correct": False}
        ]
    },
    {
        "text": "What must be done to configure an IP address on an interface?",
        "choices": [
            {"text": "Enter interface view", "is_correct": True},
            {"text": "Run ip address command", "is_correct": True},
            {"text": "Set DNS server", "is_correct": False},
            {"text": "Ensure the interface is enabled", "is_correct": True}
        ]
    },
    {
        "text": "What commands are used to configure the time zone and system time?",
        "choices": [
            {"text": "clock timezone", "is_correct": True},
            {"text": "clock datetime utc", "is_correct": True},
            {"text": "set time", "is_correct": False},
            {"text": "clock datetime", "is_correct": True}
        ]
    },
    {
        "text": "What actions occur when you run the save command?",
        "choices": [
            {"text": "Save current configuration", "is_correct": True},
            {"text": "Create a backup file", "is_correct": True},
            {"text": "Save to flash", "is_correct": True},
            {"text": "Reset device", "is_correct": False}
        ]
    },
    {
        "text": "Which features are provided by BootROM?",
        "choices": [
            {"text": "Startup self-check", "is_correct": True},
            {"text": "User access control", "is_correct": False},
            {"text": "System auto start", "is_correct": True},
            {"text": "Protocol conversion", "is_correct": False}
        ]
    },
    {
        "text": "Which of the following apply to the loopback interface?",
        "choices": [
            {"text": "Reliable", "is_correct": True},
            {"text": "Used as management interface", "is_correct": True},
            {"text": "Used for ARP requests", "is_correct": False},
            {"text": "Virtual/logical interface", "is_correct": True}
        ]
    }
]

# Questions vrai/faux
true_false_questions = [
    {
        "text": "The console port login function is disabled by default.",
        "choices": [
            {"text": "True", "is_correct": False},
            {"text": "False", "is_correct": True}
        ]
    },
    {
        "text": "A file deleted with /unreserved cannot be restored.",
        "choices": [
            {"text": "True", "is_correct": True},
            {"text": "False", "is_correct": False}
        ]
    },
    {
        "text": "The pwd command displays the contents of a file.",
        "choices": [
            {"text": "True", "is_correct": False},
            {"text": "False", "is_correct": True}
        ]
    },
    {
        "text": "The command undo shutdown is used to enable an interface.",
        "choices": [
            {"text": "True", "is_correct": True},
            {"text": "False", "is_correct": False}
        ]
    },
    {
        "text": "VTY connections are physical connections to the device.",
        "choices": [
            {"text": "True", "is_correct": False},
            {"text": "False", "is_correct": True}
        ]
    }
]

# Création des listes pour chaque type de question
all_questions = []

# Ajouter les questions à choix unique avec le flag is_multiple_choice=False
for q in single_choice_questions:
    q["is_multiple_choice"] = False
    all_questions.append(q)

# Ajouter les questions à choix multiples avec le flag is_multiple_choice=True
for q in multiple_choice_questions:
    q["is_multiple_choice"] = True
    all_questions.append(q)

# Ajouter les questions vrai/faux avec le flag is_multiple_choice=False
for q in true_false_questions:
    q["is_multiple_choice"] = False
    all_questions.append(q)

# Créer les questions et les choix
for i, q_data in enumerate(all_questions, 1):
    question = Question.objects.create(
        quiz=quiz,
        text=q_data["text"],
        explanation="",  # Pas d'explication
        order=i,
        is_multiple_choice=q_data["is_multiple_choice"]
    )
    
    # Ajout des choix
    for choice_data in q_data["choices"]:
        Choice.objects.create(
            question=question,
            text=choice_data["text"],
            is_correct=choice_data["is_correct"]
        )
    
    question_type = "choix multiples" if q_data["is_multiple_choice"] else "choix unique"
    print(f"Question {i} ajoutée ({question_type}) avec {len(q_data['choices'])} choix")

print(f"\nQuiz Huawei Device Commands créé avec succès avec {len(single_choice_questions)} questions à choix unique, {len(multiple_choice_questions)} questions à choix multiples, et {len(true_false_questions)} questions vrai/faux.")
