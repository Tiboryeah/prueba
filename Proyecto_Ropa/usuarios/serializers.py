# usuarios/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Serializer para el registro
class SignupSerializer(serializers.ModelSerializer):
    # El username será el email
    username = serializers.CharField(max_length=150, required=False)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        # Si no se pasa un username, lo asignamos al email
        username = validated_data.get('username', validated_data['email'])
        
        user = User.objects.create_user(
            username=username,  # Usamos el email como username si no se proporciona otro
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']  # La contraseña se encriptará automáticamente
        )
        return user
    
# Serializer para el login
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Verificamos si el usuario existe con el email
        user = User.objects.filter(email=data['email']).first()
        if user is None:
            raise serializers.ValidationError("El correo electrónico no está registrado.")
        
        # Intentamos autenticar al usuario
        user = authenticate(username=data['email'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Correo electrónico o contraseña incorrectos.")
        
        return {'user': user}
