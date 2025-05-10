import os
import django
import json
import requests

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

def test_register_user():
    # URL de l'API d'inscription
    api_url = "https://quizapp-xqwn.onrender.com/api/users/register/"
    
    # Données d'inscription avec un nom d'utilisateur différent
    user_data = {
        "username": "testuser456",
        "email": "testuser456@example.com",
        "password": "TestPassword456",
        "password2": "TestPassword456"
    }
    
    # En-têtes de la requête
    headers = {
        "Content-Type": "application/json"
    }
    
    # Envoi de la requête POST
    print(f"Envoi d'une requête d'inscription à {api_url}")
    print(f"Données: {json.dumps(user_data, indent=2)}")
    
    try:
        response = requests.post(api_url, json=user_data, headers=headers)
        
        # Affichage de la réponse
        print(f"\nCode de statut: {response.status_code}")
        print(f"Contenu de la réponse: {response.text}")
        
        if response.status_code == 201:
            print("\nInscription réussie! L'utilisateur a été créé.")
            print("\nVous pouvez maintenant vous connecter avec:")
            print(f"Username: {user_data['username']}")
            print(f"Password: {user_data['password']}")
        else:
            print("\nL'inscription a échoué. Vérifiez les détails de l'erreur ci-dessus.")
            
            # Si nous avons une réponse JSON, essayons de l'analyser pour plus de détails
            try:
                error_data = response.json()
                print("\nDétails de l'erreur:")
                for field, errors in error_data.items():
                    print(f"  {field}: {errors}")
            except:
                pass
    
    except Exception as e:
        print(f"\nUne erreur s'est produite: {str(e)}")

if __name__ == "__main__":
    print("Test d'inscription d'un nouvel utilisateur...")
    test_register_user()
