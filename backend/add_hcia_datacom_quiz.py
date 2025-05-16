import os
import django
import sys

# Configure Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from django.contrib.auth import get_user_model
from quizzes.models import Quiz, Question, Choice

User = get_user_model()

def create_hcia_datacom_quiz():
    # Create or get admin user
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
        print("Admin user created successfully.")
    
    # Create the quiz
    quiz, created = Quiz.objects.get_or_create(
        title="HCIA Datacom Practice Questions - Chapter 1",
        defaults={
            'description': "25 HCIA Datacom practice questions covering data communication network basics",
            'subject': "Networking",
            'difficulty': "medium",
            'time_limit': 25
        }
    )
    
    if created:
        print(f"Quiz '{quiz.title}' created successfully.")
    else:
        print(f"Quiz '{quiz.title}' already exists.")
        # Delete existing questions to avoid duplicates
        Question.objects.filter(quiz=quiz).delete()
        print("Existing questions deleted.")
    
    # List of questions and answers
    questions_data = [
        # Single Choice Questions (1-10)
        {
            "text": "What device is typically closest to the end user in a campus network?",
            "explanation": "In a campus network, switches are typically the devices closest to end users, providing direct connectivity to user devices.",
            "choices": [
                {"text": "Router", "is_correct": False},
                {"text": "Gateway", "is_correct": False},
                {"text": "Switch", "is_correct": True},
                {"text": "Firewall", "is_correct": False}
            ]
        },
        {
            "text": "What is the main function of a gateway?",
            "explanation": "Gateways primarily handle protocol conversion and route selection between different networks, allowing systems with different protocols to communicate.",
            "choices": [
                {"text": "Connecting terminals", "is_correct": False},
                {"text": "Routing between LANs", "is_correct": False},
                {"text": "Protocol conversion and route selection", "is_correct": True},
                {"text": "Assigning IP addresses", "is_correct": False}
            ]
        },
        {
            "text": "Which topology requires the most cabling and physical ports?",
            "explanation": "A full-mesh topology requires direct connections between all nodes, resulting in the highest number of cables and physical ports compared to other topologies.",
            "choices": [
                {"text": "Ring topology", "is_correct": False},
                {"text": "Star topology", "is_correct": False},
                {"text": "Bus topology", "is_correct": False},
                {"text": "Full-mesh topology", "is_correct": True}
            ]
        },
        {
            "text": "What does encapsulation refer to in data communication?",
            "explanation": "Encapsulation is the process of adding protocol headers and trailers to data as it moves down the network stack, preparing it for transmission.",
            "choices": [
                {"text": "Splitting a message into smaller packets", "is_correct": False},
                {"text": "Removing headers from packets", "is_correct": False},
                {"text": "Adding headers and tails to data payload", "is_correct": True},
                {"text": "Compressing packet data", "is_correct": False}
            ]
        },
        {
            "text": "Which device is used to isolate broadcast domains?",
            "explanation": "Routers operate at Layer 3 and isolate broadcast domains, preventing broadcast traffic from propagating between different networks.",
            "choices": [
                {"text": "Switch", "is_correct": False},
                {"text": "Router", "is_correct": True},
                {"text": "AP", "is_correct": False},
                {"text": "Terminal", "is_correct": False}
            ]
        },
        {
            "text": "What is a common disadvantage of the bus topology?",
            "explanation": "Bus topology has several disadvantages, but a significant one is that if the main cable fails, the entire network goes down, making it less secure than other topologies.",
            "choices": [
                {"text": "Complex cabling", "is_correct": False},
                {"text": "Difficult node addition", "is_correct": False},
                {"text": "Low security", "is_correct": True},
                {"text": "High cost", "is_correct": False}
            ]
        },
        {
            "text": "Which device works at the network layer of the TCP/IP model?",
            "explanation": "Routers operate at the network layer (Layer 3) of the TCP/IP model, making routing decisions based on IP addresses.",
            "choices": [
                {"text": "Layer 2 Switch", "is_correct": False},
                {"text": "Router", "is_correct": True},
                {"text": "Firewall", "is_correct": False},
                {"text": "Access Point", "is_correct": False}
            ]
        },
        {
            "text": "Which wireless architecture is recommended for large enterprises?",
            "explanation": "Fit AP architecture is recommended for large enterprises as it centralizes management and control through wireless controllers, making large deployments more manageable.",
            "choices": [
                {"text": "Fat AP", "is_correct": False},
                {"text": "Fit AP", "is_correct": True},
                {"text": "Cloud-managed AP", "is_correct": False},
                {"text": "Ethernet AP", "is_correct": False}
            ]
        },
        {
            "text": "What is the correct order of packet handling from source to destination?",
            "explanation": "In packet formation, the data is first identified, then a header is added to provide routing and control information, followed by a tail for error checking.",
            "choices": [
                {"text": "Packet > Tail > Header", "is_correct": False},
                {"text": "Header > Data > Tail", "is_correct": True},
                {"text": "Data > Header > Tail", "is_correct": False},
                {"text": "Tail > Header > Data", "is_correct": False}
            ]
        },
        {
            "text": "Which of the following technologies is NOT typically used in WAN?",
            "explanation": "Ethernet is primarily a LAN technology, while PPP, WiMAX, and HDLC are commonly used in WAN environments.",
            "choices": [
                {"text": "PPP", "is_correct": False},
                {"text": "WiMAX", "is_correct": False},
                {"text": "HDLC", "is_correct": False},
                {"text": "Ethernet", "is_correct": True}
            ]
        },
        
        # Multiple Choice Questions (11-20)
        {
            "text": "Which of the following are components of a packet? (Select all that apply)",
            "explanation": "A packet consists of a header (containing control information), payload (the actual data), and a tail/trailer (containing error checking information).",
            "choices": [
                {"text": "Header", "is_correct": True},
                {"text": "Payload", "is_correct": True},
                {"text": "Protocol", "is_correct": False},
                {"text": "Tail", "is_correct": True}
            ]
        },
        {
            "text": "Which devices can be considered terminal devices? (Select all that apply)",
            "explanation": "Terminal devices are end-user devices that serve as data sources or destinations. Servers, VoIP phones, and mobile phones are all terminal devices, while routers are intermediary network devices.",
            "choices": [
                {"text": "Server", "is_correct": True},
                {"text": "VoIP phone", "is_correct": True},
                {"text": "Router", "is_correct": False},
                {"text": "Mobile phone", "is_correct": True}
            ]
        },
        {
            "text": "Which are characteristics of a MAN (Metropolitan Area Network)? (Select all that apply)",
            "explanation": "MANs connect LANs within a city area and support high-speed transmission, but they don't typically use coaxial bus cabling and are not cheaper than LANs.",
            "choices": [
                {"text": "Connects distant LANs in a city", "is_correct": True},
                {"text": "Uses coaxial bus cabling", "is_correct": False},
                {"text": "Supports high-speed transmission", "is_correct": True},
                {"text": "Typically cheaper than LAN", "is_correct": False}
            ]
        },
        {
            "text": "Which functions are performed by routers? (Select all that apply)",
            "explanation": "Routers perform data forwarding, route discovery, and isolate broadcast domains. They don't provide WLAN access (that's an AP's function).",
            "choices": [
                {"text": "Data forwarding", "is_correct": True},
                {"text": "Route discovery", "is_correct": True},
                {"text": "WLAN access", "is_correct": False},
                {"text": "Broadcast domain isolation", "is_correct": True}
            ]
        },
        {
            "text": "Which of the following can describe WLAN technologies? (Select all that apply)",
            "explanation": "WLANs use radio waves for transmission, include fat and fit APs as architecture options, and many modern solutions support cloud management. They do not require coaxial cables.",
            "choices": [
                {"text": "Use radio waves", "is_correct": True},
                {"text": "Include fat and fit APs", "is_correct": True},
                {"text": "Require coaxial cables", "is_correct": False},
                {"text": "May support cloud management", "is_correct": True}
            ]
        },
        {
            "text": "Which statements are true about encapsulation? (Select all that apply)",
            "explanation": "Encapsulation adds headers to data and facilitates layered communication. It happens at multiple layers, not just on routers, and doesn't involve data compression.",
            "choices": [
                {"text": "Adds headers to data", "is_correct": True},
                {"text": "Happens only on routers", "is_correct": False},
                {"text": "Facilitates layered communication", "is_correct": True},
                {"text": "Involves compression of data", "is_correct": False}
            ]
        },
        {
            "text": "Which features are provided by firewalls? (Select all that apply)",
            "explanation": "Firewalls provide unified security policy enforcement and prevent unauthorized access. They don't typically handle wireless management or packet switching.",
            "choices": [
                {"text": "Unified security policy enforcement", "is_correct": True},
                {"text": "Wireless management", "is_correct": False},
                {"text": "Unauthorized access prevention", "is_correct": True},
                {"text": "Packet switching", "is_correct": False}
            ]
        },
        {
            "text": "Which topologies allow easy addition of new nodes? (Select all that apply)",
            "explanation": "Star and tree topologies allow easy addition of new nodes without disrupting the entire network. Bus topology requires tapping into the main cable, and ring topology requires breaking the ring.",
            "choices": [
                {"text": "Star topology", "is_correct": True},
                {"text": "Bus topology", "is_correct": False},
                {"text": "Tree topology", "is_correct": True},
                {"text": "Ring topology", "is_correct": False}
            ]
        },
        {
            "text": "Which network types are typically based on geographic coverage? (Select all that apply)",
            "explanation": "LAN, MAN, and WAN are all classified based on their geographic coverage area. SAN (Storage Area Network) is classified by its function, not geography.",
            "choices": [
                {"text": "LAN", "is_correct": True},
                {"text": "MAN", "is_correct": True},
                {"text": "WAN", "is_correct": True},
                {"text": "SAN", "is_correct": False}
            ]
        },
        {
            "text": "Which of the following are considered functions of a Layer 2 switch? (Select all that apply)",
            "explanation": "Layer 2 switches perform data frame switching, provide end-user access, and support Layer 2 redundancy protocols. They don't route between subnets (that's a Layer 3 function).",
            "choices": [
                {"text": "Data frame switching", "is_correct": True},
                {"text": "Routing between subnets", "is_correct": False},
                {"text": "End-user access", "is_correct": True},
                {"text": "Layer 2 redundancy", "is_correct": True}
            ]
        },
        
        # True or False Questions (21-25)
        {
            "text": "A packet always contains a tail segment. (True/False)",
            "explanation": "False. Not all packets contain a tail segment. Some protocols and implementations may omit the tail or trailer, especially if error checking is handled at a different layer.",
            "choices": [
                {"text": "True", "is_correct": False},
                {"text": "False", "is_correct": True}
            ]
        },
        {
            "text": "Fit APs require an AC for configuration and management. (True/False)",
            "explanation": "True. Fit APs (also called lightweight APs) rely on an Access Controller (AC) for configuration, management, and control functions.",
            "choices": [
                {"text": "True", "is_correct": True},
                {"text": "False", "is_correct": False}
            ]
        },
        {
            "text": "Routers work at the transport layer of the TCP/IP model. (True/False)",
            "explanation": "False. Routers work at the network layer (Layer 3) of the TCP/IP model, not the transport layer (Layer 4).",
            "choices": [
                {"text": "True", "is_correct": False},
                {"text": "False", "is_correct": True}
            ]
        },
        {
            "text": "Tree topology is a hierarchical version of star topology. (True/False)",
            "explanation": "True. Tree topology is essentially a hierarchical extension of the star topology, where multiple star networks are connected in a hierarchical structure.",
            "choices": [
                {"text": "True", "is_correct": True},
                {"text": "False", "is_correct": False}
            ]
        },
        {
            "text": "In a full-mesh network, cost and scalability are major disadvantages. (True/False)",
            "explanation": "True. In a full-mesh network, every node is connected to every other node, which leads to high costs and poor scalability as the number of required connections grows exponentially with each new node.",
            "choices": [
                {"text": "True", "is_correct": True},
                {"text": "False", "is_correct": False}
            ]
        }
    ]
    
    # Add questions and choices
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
        
        print(f"Question {i} added: {q_data['text'][:50]}...")
    
    print(f"\nQuiz '{quiz.title}' with {len(questions_data)} questions has been created successfully!")
    return quiz

if __name__ == "__main__":
    print("Creating HCIA Datacom practice questions quiz...")
    create_hcia_datacom_quiz()
