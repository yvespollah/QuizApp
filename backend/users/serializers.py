from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user objects"""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio']
        read_only_fields = ['id']


class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating user objects"""
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    bio = serializers.CharField(required=False, allow_blank=True, default='')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'bio']

    def validate_email(self, value):
        # Vérifier si l'email existe déjà
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Un utilisateur avec cet email existe déjà.")
        return value

    def validate_username(self, value):
        # Vérifier si le nom d'utilisateur existe déjà
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Ce nom d'utilisateur est déjà pris.")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas."})
        return attrs

    def create(self, validated_data):
        try:
            # Supprimer password2 avant de créer l'utilisateur
            validated_data.pop('password2')
            # Créer l'utilisateur
            user = User.objects.create_user(**validated_data)
            return user
        except Exception as e:
            # Capturer toute erreur lors de la création de l'utilisateur
            raise serializers.ValidationError({"detail": f"Erreur lors de la création de l'utilisateur: {str(e)}"})


class UserUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating user objects"""
    
    class Meta:
        model = User
        fields = ['username', 'email', 'bio']
        read_only_fields = ['email']  # Email cannot be changed
