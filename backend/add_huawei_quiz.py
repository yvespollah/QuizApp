import os
import django
import sys

# Configurer l'environnement Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from django.contrib.auth import get_user_model
from quizzes.models import Quiz, Question, Choice

User = get_user_model()

def create_huawei_datacommunication_quiz():
    # Créer ou récupérer un utilisateur admin
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@example.com',
            'is_staff': True,
            'is_superuser': True
        }
    )
    
    if created:
        admin_user.set_password('admin123')
        admin_user.save()
        print("Utilisateur admin créé avec succès.")
    
    # Créer le quiz
    quiz, created = Quiz.objects.get_or_create(
        title="Communications de données Huawei",
        defaults={
            'description': "Quiz sur les principes fondamentaux des communications de données selon Huawei",
            'subject': "Réseaux",
            'difficulty': "medium",
            'time_limit': 30
        }
    )
    
    if created:
        print(f"Quiz '{quiz.title}' créé avec succès.")
    else:
        print(f"Quiz '{quiz.title}' existe déjà.")
        # Supprimer les questions existantes pour éviter les doublons
        Question.objects.filter(quiz=quiz).delete()
        print("Questions existantes supprimées.")
    
    # Liste des questions et réponses
    questions_data = [
        {
            "text": "Quel protocole est utilisé pour la configuration dynamique des adresses IP dans les réseaux Huawei?",
            "explanation": "DHCP (Dynamic Host Configuration Protocol) est utilisé pour attribuer automatiquement des adresses IP aux appareils du réseau.",
            "choices": [
                {"text": "DHCP", "is_correct": True},
                {"text": "SMTP", "is_correct": False},
                {"text": "FTP", "is_correct": False},
                {"text": "HTTP", "is_correct": False}
            ]
        },
        {
            "text": "Quelle est la fonction principale d'un routeur Huawei dans un réseau?",
            "explanation": "Un routeur Huawei dirige les paquets de données entre différents réseaux en utilisant les informations de routage.",
            "choices": [
                {"text": "Amplifier les signaux électriques", "is_correct": False},
                {"text": "Connecter des périphériques au réseau local", "is_correct": False},
                {"text": "Diriger les paquets de données entre différents réseaux", "is_correct": True},
                {"text": "Stocker des données en masse", "is_correct": False}
            ]
        },
        {
            "text": "Quel est le protocole de routage propriétaire développé par Huawei?",
            "explanation": "Huawei a développé le protocole EBGP (Enhanced Border Gateway Protocol) comme une version améliorée du BGP standard.",
            "choices": [
                {"text": "OSPF", "is_correct": False},
                {"text": "RIP", "is_correct": False},
                {"text": "EBGP", "is_correct": True},
                {"text": "EIGRP", "is_correct": False}
            ]
        },
        {
            "text": "Quelle technologie Huawei utilise pour la virtualisation des réseaux?",
            "explanation": "SDN (Software-Defined Networking) est la technologie utilisée par Huawei pour la virtualisation des réseaux, permettant une gestion centralisée.",
            "choices": [
                {"text": "SDN", "is_correct": True},
                {"text": "MPLS", "is_correct": False},
                {"text": "VPN", "is_correct": False},
                {"text": "NAT", "is_correct": False}
            ]
        },
        {
            "text": "Quel est le système d'exploitation réseau propriétaire de Huawei?",
            "explanation": "VRP (Versatile Routing Platform) est le système d'exploitation réseau propriétaire de Huawei utilisé dans ses équipements de réseau.",
            "choices": [
                {"text": "IOS", "is_correct": False},
                {"text": "VRP", "is_correct": True},
                {"text": "JUNOS", "is_correct": False},
                {"text": "EOS", "is_correct": False}
            ]
        },
        {
            "text": "Quelle est la vitesse maximale théorique de la technologie 5G de Huawei?",
            "explanation": "La technologie 5G de Huawei peut atteindre théoriquement jusqu'à 10 Gbps dans des conditions idéales.",
            "choices": [
                {"text": "1 Gbps", "is_correct": False},
                {"text": "10 Gbps", "is_correct": True},
                {"text": "100 Mbps", "is_correct": False},
                {"text": "100 Gbps", "is_correct": False}
            ]
        },
        {
            "text": "Quelle technologie Huawei utilise pour améliorer la sécurité des communications de données?",
            "explanation": "IPSec (Internet Protocol Security) est utilisé par Huawei pour sécuriser les communications IP en authentifiant et chiffrant chaque paquet IP.",
            "choices": [
                {"text": "WEP", "is_correct": False},
                {"text": "SSL", "is_correct": False},
                {"text": "IPSec", "is_correct": True},
                {"text": "HTTP", "is_correct": False}
            ]
        },
        {
            "text": "Quel protocole est utilisé pour la gestion à distance des équipements réseau Huawei?",
            "explanation": "SNMP (Simple Network Management Protocol) est utilisé pour surveiller et gérer à distance les équipements réseau Huawei.",
            "choices": [
                {"text": "SMTP", "is_correct": False},
                {"text": "SNMP", "is_correct": True},
                {"text": "SSH", "is_correct": False},
                {"text": "Telnet", "is_correct": False}
            ]
        },
        {
            "text": "Quelle est la technologie de Huawei pour l'interconnexion des centres de données?",
            "explanation": "CloudFabric est la solution de Huawei pour l'interconnexion des centres de données, offrant une architecture réseau évolutive et flexible.",
            "choices": [
                {"text": "CloudEngine", "is_correct": False},
                {"text": "CloudFabric", "is_correct": True},
                {"text": "CloudLink", "is_correct": False},
                {"text": "CloudWAN", "is_correct": False}
            ]
        },
        {
            "text": "Quel est le protocole utilisé pour la synchronisation temporelle dans les réseaux Huawei?",
            "explanation": "NTP (Network Time Protocol) est utilisé pour synchroniser les horloges des systèmes informatiques sur les réseaux Huawei.",
            "choices": [
                {"text": "NTP", "is_correct": True},
                {"text": "SNTP", "is_correct": False},
                {"text": "PTP", "is_correct": False},
                {"text": "TCP", "is_correct": False}
            ]
        },
        {
            "text": "Quelle est la solution de Huawei pour l'automatisation des réseaux?",
            "explanation": "NCE (Network Cloud Engine) est la solution de Huawei pour l'automatisation des réseaux, offrant des capacités d'orchestration et d'analyse.",
            "choices": [
                {"text": "NCE", "is_correct": True},
                {"text": "iMaster", "is_correct": False},
                {"text": "CloudCampus", "is_correct": False},
                {"text": "NetOpen", "is_correct": False}
            ]
        },
        {
            "text": "Quelle technologie Huawei utilise pour l'agrégation de liens?",
            "explanation": "LACP (Link Aggregation Control Protocol) est utilisé pour combiner plusieurs connexions réseau en parallèle afin d'augmenter le débit.",
            "choices": [
                {"text": "VLAN", "is_correct": False},
                {"text": "LACP", "is_correct": True},
                {"text": "STP", "is_correct": False},
                {"text": "OSPF", "is_correct": False}
            ]
        },
        {
            "text": "Quelle est la solution de Huawei pour les réseaux campus intelligents?",
            "explanation": "CloudCampus est la solution de Huawei pour les réseaux campus intelligents, offrant une gestion simplifiée et une expérience utilisateur améliorée.",
            "choices": [
                {"text": "CloudEngine", "is_correct": False},
                {"text": "CloudCampus", "is_correct": True},
                {"text": "CloudCore", "is_correct": False},
                {"text": "CloudWAN", "is_correct": False}
            ]
        },
        {
            "text": "Quel est le protocole de tunneling utilisé dans les solutions VPN de Huawei?",
            "explanation": "GRE (Generic Routing Encapsulation) est un protocole de tunneling utilisé dans les solutions VPN de Huawei pour encapsuler divers protocoles réseau.",
            "choices": [
                {"text": "L2TP", "is_correct": False},
                {"text": "PPTP", "is_correct": False},
                {"text": "GRE", "is_correct": True},
                {"text": "IPSec", "is_correct": False}
            ]
        },
        {
            "text": "Quelle est la technologie de Huawei pour les réseaux définis par logiciel?",
            "explanation": "Agile Controller est la plateforme SDN de Huawei qui permet de centraliser la gestion et le contrôle des réseaux.",
            "choices": [
                {"text": "Agile Controller", "is_correct": True},
                {"text": "VRP", "is_correct": False},
                {"text": "CloudEngine", "is_correct": False},
                {"text": "iMaster", "is_correct": False}
            ]
        },
        {
            "text": "Quel est le protocole utilisé pour la redondance de passerelle dans les réseaux Huawei?",
            "explanation": "VRRP (Virtual Router Redundancy Protocol) est utilisé pour fournir une redondance automatique pour les passerelles par défaut.",
            "choices": [
                {"text": "HSRP", "is_correct": False},
                {"text": "VRRP", "is_correct": True},
                {"text": "GLBP", "is_correct": False},
                {"text": "STP", "is_correct": False}
            ]
        },
        {
            "text": "Quelle est la solution de Huawei pour l'analyse du trafic réseau?",
            "explanation": "iMaster NCE-FabricInsight est la solution de Huawei pour l'analyse du trafic réseau, offrant une visibilité en temps réel et des capacités d'analyse avancées.",
            "choices": [
                {"text": "NetStream", "is_correct": False},
                {"text": "iMaster NCE-FabricInsight", "is_correct": True},
                {"text": "CloudMetrics", "is_correct": False},
                {"text": "NetworkAnalyzer", "is_correct": False}
            ]
        },
        {
            "text": "Quelle technologie Huawei utilise pour la qualité de service (QoS) dans les réseaux?",
            "explanation": "DiffServ (Differentiated Services) est utilisé par Huawei pour implémenter la qualité de service en classifiant et en priorisant différents types de trafic.",
            "choices": [
                {"text": "IntServ", "is_correct": False},
                {"text": "DiffServ", "is_correct": True},
                {"text": "RSVP", "is_correct": False},
                {"text": "ToS", "is_correct": False}
            ]
        },
        {
            "text": "Quelle est la solution de Huawei pour les réseaux optiques passifs?",
            "explanation": "GPON (Gigabit Passive Optical Network) est la technologie utilisée par Huawei pour les réseaux optiques passifs à haut débit.",
            "choices": [
                {"text": "EPON", "is_correct": False},
                {"text": "GPON", "is_correct": True},
                {"text": "BPON", "is_correct": False},
                {"text": "APON", "is_correct": False}
            ]
        },
        {
            "text": "Quel est le protocole de routage utilisé dans les grandes entreprises avec équipements Huawei?",
            "explanation": "OSPF (Open Shortest Path First) est un protocole de routage à état de lien largement utilisé dans les réseaux d'entreprise équipés de matériel Huawei.",
            "choices": [
                {"text": "RIP", "is_correct": False},
                {"text": "OSPF", "is_correct": True},
                {"text": "BGP", "is_correct": False},
                {"text": "EIGRP", "is_correct": False}
            ]
        }
    ]
    
    # Ajouter les questions et les choix
    for i, q_data in enumerate(questions_data, 1):
        question = Question.objects.create(
            quiz=quiz,
            text=q_data["text"],
            explanation=q_data["explanation"],
            order=i
        )
        
        for c_data in q_data["choices"]:
            Choice.objects.create(
                question=question,
                text=c_data["text"],
                is_correct=c_data["is_correct"]
            )
        
        print(f"Question {i} ajoutée: {q_data['text'][:50]}...")
    
    print(f"\nQuiz '{quiz.title}' avec {len(questions_data)} questions a été créé avec succès!")
    return quiz

if __name__ == "__main__":
    print("Création du quiz sur les communications de données Huawei...")
    create_huawei_datacommunication_quiz()
