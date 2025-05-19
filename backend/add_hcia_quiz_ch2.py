#!/usr/bin/env python
import os
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quizzes.models import Quiz, Question, Choice

# Création du quiz
quiz = Quiz.objects.create(
    title="HCIA Datacom Chapter 2 Practice Questions",
    description="25 HCIA Datacom practice questions covering TCP/IP and OSI models, protocols, and network communication concepts.",
    subject="Huawei HCIA Datacom",
    difficulty="medium",
    time_limit=20  # 20 minutes
)

print(f"Quiz créé: {quiz.title}")

# Questions à choix unique
single_choice_questions = [
    {
        "text": "Which OSI layer is responsible for converting data into a format suitable for transmission over physical media?",
        "choices": [
            {"text": "Data Link Layer", "is_correct": False},
            {"text": "Presentation Layer", "is_correct": False},
            {"text": "Physical Layer", "is_correct": True},
            {"text": "Application Layer", "is_correct": False}
        ]
    },
    {
        "text": "Which protocol is used for translating domain names into IP addresses?",
        "choices": [
            {"text": "HTTP", "is_correct": False},
            {"text": "FTP", "is_correct": False},
            {"text": "DNS", "is_correct": True},
            {"text": "ICMP", "is_correct": False}
        ]
    },
    {
        "text": "What is the size of a TCP Sequence Number field?",
        "choices": [
            {"text": "8 bits", "is_correct": False},
            {"text": "16 bits", "is_correct": False},
            {"text": "32 bits", "is_correct": True},
            {"text": "64 bits", "is_correct": False}
        ]
    },
    {
        "text": "Which TCP control flag is used to initiate a connection?",
        "choices": [
            {"text": "ACK", "is_correct": False},
            {"text": "FIN", "is_correct": False},
            {"text": "URG", "is_correct": False},
            {"text": "SYN", "is_correct": True}
        ]
    },
    {
        "text": "Which protocol is connectionless and does not guarantee delivery?",
        "choices": [
            {"text": "TCP", "is_correct": False},
            {"text": "FTP", "is_correct": False},
            {"text": "UDP", "is_correct": True},
            {"text": "HTTP", "is_correct": False}
        ]
    },
    {
        "text": "In which layer of the TCP/IP model is the Ethernet protocol located?",
        "choices": [
            {"text": "Network Layer", "is_correct": False},
            {"text": "Application Layer", "is_correct": False},
            {"text": "Transport Layer", "is_correct": False},
            {"text": "Data Link Layer", "is_correct": True}
        ]
    },
    {
        "text": "What is the main role of ARP in a network?",
        "choices": [
            {"text": "IP address allocation", "is_correct": False},
            {"text": "Name resolution", "is_correct": False},
            {"text": "MAC address resolution", "is_correct": True},
            {"text": "Traffic encryption", "is_correct": False}
        ]
    },
    {
        "text": "What field in a TCP header is used for flow control?",
        "choices": [
            {"text": "Sequence Number", "is_correct": False},
            {"text": "Acknowledgment Number", "is_correct": False},
            {"text": "Window", "is_correct": True},
            {"text": "Checksum", "is_correct": False}
        ]
    },
    {
        "text": "Which protocol sends error and diagnostic messages on the network layer?",
        "choices": [
            {"text": "ARP", "is_correct": False},
            {"text": "ICMP", "is_correct": True},
            {"text": "TCP", "is_correct": False},
            {"text": "UDP", "is_correct": False}
        ]
    },
    {
        "text": "Which type of cable is most commonly used in Ethernet LANs?",
        "choices": [
            {"text": "Serial cable", "is_correct": False},
            {"text": "Coaxial cable", "is_correct": False},
            {"text": "Optical fiber", "is_correct": False},
            {"text": "Twisted pair", "is_correct": True}
        ]
    }
]

# Questions à choix multiples
multiple_choice_questions = [
    {
        "text": "Which protocols operate at the transport layer?",
        "choices": [
            {"text": "TCP", "is_correct": True},
            {"text": "UDP", "is_correct": True},
            {"text": "ICMP", "is_correct": False},
            {"text": "HTTP", "is_correct": False}
        ]
    },
    {
        "text": "Which are characteristics of UDP?",
        "choices": [
            {"text": "Reliable", "is_correct": False},
            {"text": "Connectionless", "is_correct": True},
            {"text": "Lightweight", "is_correct": True},
            {"text": "Ordered transmission", "is_correct": False}
        ]
    },
    {
        "text": "What information is found in a TCP header?",
        "choices": [
            {"text": "Sequence Number", "is_correct": True},
            {"text": "Source Port", "is_correct": True},
            {"text": "TTL", "is_correct": False},
            {"text": "Window", "is_correct": True}
        ]
    },
    {
        "text": "Which OSI layers deal directly with end-user applications and data presentation?",
        "choices": [
            {"text": "Presentation Layer", "is_correct": True},
            {"text": "Application Layer", "is_correct": True},
            {"text": "Data Link Layer", "is_correct": False},
            {"text": "Session Layer", "is_correct": True}
        ]
    },
    {
        "text": "Which of the following are valid functions of ARP?",
        "choices": [
            {"text": "Duplicate IP detection", "is_correct": True},
            {"text": "IP to MAC mapping", "is_correct": True},
            {"text": "Routing between networks", "is_correct": False},
            {"text": "MAC address caching", "is_correct": True}
        ]
    },
    {
        "text": "Which protocols are commonly used at the data link layer?",
        "choices": [
            {"text": "PPP", "is_correct": True},
            {"text": "PPPoE", "is_correct": True},
            {"text": "Ethernet", "is_correct": True},
            {"text": "IP", "is_correct": False}
        ]
    },
    {
        "text": "What happens during a TCP three-way handshake?",
        "choices": [
            {"text": "SYN flag is used", "is_correct": True},
            {"text": "ACK flag is used", "is_correct": True},
            {"text": "FIN flag is used", "is_correct": False},
            {"text": "Ports are negotiated", "is_correct": True}
        ]
    },
    {
        "text": "What are typical PDUs (Protocol Data Units) at each layer?",
        "choices": [
            {"text": "Bits (Physical)", "is_correct": True},
            {"text": "Frames (Data Link)", "is_correct": True},
            {"text": "Segments (Transport)", "is_correct": True},
            {"text": "Signals (Application)", "is_correct": False}
        ]
    },
    {
        "text": "Which types of media can be used for physical transmission?",
        "choices": [
            {"text": "Electrical signals", "is_correct": True},
            {"text": "Optical fiber", "is_correct": True},
            {"text": "Electromagnetic waves", "is_correct": True},
            {"text": "JSON", "is_correct": False}
        ]
    },
    {
        "text": "What happens when an ARP entry expires?",
        "choices": [
            {"text": "Data is dropped", "is_correct": False},
            {"text": "A new ARP request is sent", "is_correct": True},
            {"text": "IP address is blocked", "is_correct": False},
            {"text": "Device disconnects", "is_correct": False}
        ]
    }
]

# Questions vrai/faux
true_false_questions = [
    {
        "text": "The TCP checksum field covers both the header and data.",
        "choices": [
            {"text": "True", "is_correct": True},
            {"text": "False", "is_correct": False}
        ]
    },
    {
        "text": "An ARP reply is always broadcast to the network.",
        "choices": [
            {"text": "True", "is_correct": False},
            {"text": "False", "is_correct": True}
        ]
    },
    {
        "text": "The MAC address is part of the OSI network layer.",
        "choices": [
            {"text": "True", "is_correct": False},
            {"text": "False", "is_correct": True}
        ]
    },
    {
        "text": "The UDP header includes both source and destination ports.",
        "choices": [
            {"text": "True", "is_correct": True},
            {"text": "False", "is_correct": False}
        ]
    },
    {
        "text": "In the OSI model, the session layer is responsible for encoding data.",
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

print(f"\nQuiz HCIA Datacom Chapter 2 créé avec succès avec {len(single_choice_questions)} questions à choix unique, {len(multiple_choice_questions)} questions à choix multiples, et {len(true_false_questions)} questions vrai/faux.")
