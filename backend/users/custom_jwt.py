import logging
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'
    
    def validate(self, attrs):
        # Log des informations de connexion (sans mot de passe)
        logger.info(f"Tentative de connexion avec email: {attrs.get('email')}")
        
        try:
            data = super().validate(attrs)
            logger.info(f"Connexion réussie pour: {attrs.get('email')}")
            return data
        except Exception as e:
            logger.error(f"Erreur de connexion pour {attrs.get('email')}: {str(e)}")
            raise

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        # Log de la requête
        logger.info(f"Requête d'authentification reçue: {request.data}")
        logger.info(f"En-têtes de la requête: {request.headers}")
        
        try:
            response = super().post(request, *args, **kwargs)
            logger.info("Réponse d'authentification générée avec succès")
            return response
        except Exception as e:
            logger.error(f"Erreur lors de l'authentification: {str(e)}")
            # Renvoyer une réponse d'erreur plus détaillée
            return Response(
                {"detail": f"Erreur d'authentification: {str(e)}", "error_type": type(e).__name__},
                status=status.HTTP_400_BAD_REQUEST
            )
