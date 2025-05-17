import logging
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer

logger = logging.getLogger(__name__)
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """View for registering new users"""
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserCreateSerializer
    
    def create(self, request, *args, **kwargs):
        # Log des informations de la requête
        logger.info(f"Requête d'inscription reçue: {request.data}")
        logger.info(f"En-têtes de la requête: {request.headers}")
        
        try:
            # Créer le sérialiseur avec les données de la requête
            serializer = self.get_serializer(data=request.data)
            
            # Vérifier si les données sont valides
            if not serializer.is_valid():
                logger.error(f"Erreurs de validation: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            # Sauvegarder l'utilisateur
            self.perform_create(serializer)
            
            # Log du succès
            logger.info(f"Utilisateur créé avec succès: {serializer.data['username']}")
            
            # Renvoyer la réponse
            headers = self.get_success_headers(serializer.data)
            return Response(
                {"detail": "Inscription réussie!", "user": serializer.data},
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        except Exception as e:
            # Log de l'erreur
            logger.error(f"Erreur lors de l'inscription: {str(e)}")
            
            # Renvoyer une réponse d'erreur détaillée
            return Response(
                {"detail": f"Erreur d'inscription: {str(e)}", "error_type": type(e).__name__},
                status=status.HTTP_400_BAD_REQUEST
            )


class UserDetailView(generics.RetrieveUpdateAPIView):
    """View for retrieving and updating user details"""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return UserUpdateSerializer
        return UserSerializer


class UserProfileView(APIView):
    """View for retrieving user profile information"""
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        # Log de la requête
        logger.info(f"Requête de profil reçue pour l'utilisateur: {request.user.username}")
        logger.info(f"En-têtes de la requête: {request.headers}")
        
        try:
            user = request.user
            serializer = UserSerializer(user)
            logger.info(f"Profil récupéré avec succès pour: {user.username}")
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Erreur lors de la récupération du profil: {str(e)}")
            return Response(
                {"detail": f"Erreur lors de la récupération du profil: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
