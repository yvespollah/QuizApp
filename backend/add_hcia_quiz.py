#!/usr/bin/env python
import os
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quizzes.models import Quiz, Question, Choice

# Création du quiz
quiz = Quiz.objects.create(
    title="HCIA Datacom Practice Questions",
    description="25 HCIA Datacom practice questions covering Data Communication Network Basis. Includes single choice, multiple choice, and true/false questions.",
    subject="Huawei HCIA Datacom",
    difficulty="medium",
    time_limit=20  # 20 minutes
)

print(f"Quiz créé: {quiz.title}")

# Questions à choix unique
single_choice_questions = [
    {
        "text": "What device is typically closest to the end user in a campus network?",
        "choices": [
            {"text": "Router", "is_correct": False},
            {"text": "Gateway", "is_correct": False},
            {"text": "Switch", "is_correct": True},
            {"text": "Firewall", "is_correct": False}
        ]
    },
    {
        "text": "What is the main function of a gateway?",
        "choices": [
            {"text": "Connecting terminals", "is_correct": False},
            {"text": "Routing between LANs", "is_correct": False},
            {"text": "Protocol conversion and route selection", "is_correct": True},
            {"text": "Assigning IP addresses", "is_correct": False}
        ]
    },
    {
        "text": "Which topology requires the most cabling and physical ports?",
        "choices": [
            {"text": "Ring topology", "is_correct": False},
            {"text": "Star topology", "is_correct": False},
            {"text": "Bus topology", "is_correct": False},
            {"text": "Full-mesh topology", "is_correct": True}
        ]
    },
    {
        "text": "What does encapsulation refer to in data communication?",
        "choices": [
            {"text": "Splitting a message into smaller packets", "is_correct": False},
            {"text": "Removing headers from packets", "is_correct": False},
            {"text": "Adding headers and tails to data payload", "is_correct": True},
            {"text": "Compressing packet data", "is_correct": False}
        ]
    },
    {
        "text": "Which device is used to isolate broadcast domains?",
        "choices": [
            {"text": "Switch", "is_correct": False},
            {"text": "Router", "is_correct": True},
            {"text": "AP", "is_correct": False},
            {"text": "Terminal", "is_correct": False}
        ]
    },
    {
        "text": "What is a common disadvantage of the bus topology?",
        "choices": [
            {"text": "Complex cabling", "is_correct": False},
            {"text": "Difficult node addition", "is_correct": False},
            {"text": "Low security", "is_correct": True},
            {"text": "High cost", "is_correct": False}
        ]
    },
    {
        "text": "Which device works at the network layer of the TCP/IP model?",
        "choices": [
            {"text": "Layer 2 Switch", "is_correct": False},
            {"text": "Router", "is_correct": True},
            {"text": "Firewall", "is_correct": False},
            {"text": "Access Point", "is_correct": False}
        ]
    },
    {
        "text": "Which wireless architecture is recommended for large enterprises?",
        "choices": [
            {"text": "Fat AP", "is_correct": False},
            {"text": "Fit AP", "is_correct": True},
            {"text": "Cloud-managed AP", "is_correct": False},
            {"text": "Ethernet AP", "is_correct": False}
        ]
    },
    {
        "text": "What is the correct order of packet handling from source to destination?",
        "choices": [
            {"text": "Packet > Tail > Header", "is_correct": False},
            {"text": "Header > Data > Tail", "is_correct": True},
            {"text": "Data > Header > Tail", "is_correct": False},
            {"text": "Tail > Header > Data", "is_correct": False}
        ]
    },
    {
        "text": "Which of the following technologies is NOT typically used in WAN?",
        "choices": [
            {"text": "PPP", "is_correct": False},
            {"text": "WiMAX", "is_correct": False},
            {"text": "HDLC", "is_correct": False},
            {"text": "Ethernet", "is_correct": True}
        ]
    }
]

# Questions à choix multiples
multiple_choice_questions = [
    {
        "text": "Which of the following are components of a packet?",
        "choices": [
            {"text": "Header", "is_correct": True},
            {"text": "Payload", "is_correct": True},
            {"text": "Protocol", "is_correct": False},
            {"text": "Tail", "is_correct": True}
        ]
    },
    {
        "text": "Which devices can be considered terminal devices?",
        "choices": [
            {"text": "Server", "is_correct": True},
            {"text": "VoIP phone", "is_correct": True},
            {"text": "Router", "is_correct": False},
            {"text": "Mobile phone", "is_correct": True}
        ]
    },
    {
        "text": "Which are characteristics of a MAN (Metropolitan Area Network)?",
        "choices": [
            {"text": "Connects distant LANs in a city", "is_correct": True},
            {"text": "Uses coaxial bus cabling", "is_correct": False},
            {"text": "Supports high-speed transmission", "is_correct": True},
            {"text": "Typically cheaper than LAN", "is_correct": False}
        ]
    },
    {
        "text": "Which functions are performed by routers?",
        "choices": [
            {"text": "Data forwarding", "is_correct": True},
            {"text": "Route discovery", "is_correct": True},
            {"text": "WLAN access", "is_correct": False},
            {"text": "Broadcast domain isolation", "is_correct": True}
        ]
    },
    {
        "text": "Which of the following can describe WLAN technologies?",
        "choices": [
            {"text": "Use radio waves", "is_correct": True},
            {"text": "Include fat and fit APs", "is_correct": True},
            {"text": "Require coaxial cables", "is_correct": False},
            {"text": "May support cloud management", "is_correct": True}
        ]
    },
    {
        "text": "Which statements are true about encapsulation?",
        "choices": [
            {"text": "Adds headers to data", "is_correct": True},
            {"text": "Happens only on routers", "is_correct": False},
            {"text": "Facilitates layered communication", "is_correct": True},
            {"text": "Involves compression of data", "is_correct": False}
        ]
    },
    {
        "text": "Which features are provided by firewalls?",
        "choices": [
            {"text": "Unified security policy enforcement", "is_correct": True},
            {"text": "Wireless management", "is_correct": False},
            {"text": "Unauthorized access prevention", "is_correct": True},
            {"text": "Packet switching", "is_correct": False}
        ]
    },
    {
        "text": "Which topologies allow easy addition of new nodes?",
        "choices": [
            {"text": "Star topology", "is_correct": True},
            {"text": "Bus topology", "is_correct": True},
            {"text": "Tree topology", "is_correct": True},
            {"text": "Ring topology", "is_correct": False}
        ]
    },
    {
        "text": "Which network types are typically based on geographic coverage?",
        "choices": [
            {"text": "LAN", "is_correct": True},
            {"text": "MAN", "is_correct": True},
            {"text": "WAN", "is_correct": True},
            {"text": "SAN", "is_correct": False}
        ]
    },
    {
        "text": "Which of the following are considered functions of a Layer 2 switch?",
        "choices": [
            {"text": "Data frame switching", "is_correct": True},
            {"text": "Routing between subnets", "is_correct": False},
            {"text": "End-user access", "is_correct": True},
            {"text": "Layer 2 redundancy", "is_correct": True}
        ]
    }
]

# Questions vrai/faux
true_false_questions = [
    {
        "text": "A packet always contains a tail segment.",
        "choices": [
            {"text": "True", "is_correct": False},
            {"text": "False", "is_correct": True}
        ]
    },
    {
        "text": "Fit APs require an AC for configuration and management.",
        "choices": [
            {"text": "True", "is_correct": True},
            {"text": "False", "is_correct": False}
        ]
    },
    {
        "text": "Routers work at the transport layer of the TCP/IP model.",
        "choices": [
            {"text": "True", "is_correct": False},
            {"text": "False", "is_correct": True}
        ]
    },
    {
        "text": "Tree topology is a hierarchical version of star topology.",
        "choices": [
            {"text": "True", "is_correct": True},
            {"text": "False", "is_correct": False}
        ]
    },
    {
        "text": "In a full-mesh network, cost and scalability are major disadvantages.",
        "choices": [
            {"text": "True", "is_correct": True},
            {"text": "False", "is_correct": False}
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

print(f"\nQuiz HCIA Datacom créé avec succès avec {len(single_choice_questions)} questions à choix unique, {len(multiple_choice_questions)} questions à choix multiples, et {len(true_false_questions)} questions vrai/faux.")
