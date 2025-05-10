import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Vérifier si l'utilisateur existe déjà
if not User.objects.filter(username='piko').exists():
    User.objects.create_superuser('piko', 'piko@example.com', '1234')
    print("Superutilisateur 'piko' créé avec succès!")
else:
    print("L'utilisateur 'piko' existe déjà.")
