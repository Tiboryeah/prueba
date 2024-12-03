# usuarios/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .models import Disenador, TipoPrenda
from django.contrib.auth.models import User

class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'Usuario registrado exitosamente',
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateDesign(APIView):
    def post(self, request):
        # Obtener el usuario actualmente autenticado
        user = request.user
        if not user.is_authenticated:
            return Response({"error": "Usuario no autenticado"}, status=status.HTTP_400_BAD_REQUEST)

        # Obtener el tipo de prenda
        tipo_prenda_nombre = request.data.get("type")
        try:
            tipo_prenda = TipoPrenda.objects.get(nombre=tipo_prenda_nombre)
        except TipoPrenda.DoesNotExist:
            return Response({"error": "Tipo de prenda no válido"}, status=status.HTTP_400_BAD_REQUEST)

        # Crear el diseño (Se agrega solo el tipo de prenda por el momento)
        diseñador = Disenador.objects.create(usuario=user, tipo_prenda=tipo_prenda)
        return Response({
            "message": "Diseño creado exitosamente",
            "disenador": {
                "id": diseñador.id,
                "nombre": diseñador.nombre,
                "tipo_prenda": diseñador.tipo_prenda.nombre,
                "usuario": diseñador.usuario.username
            }
        }, status=status.HTTP_201_CREATED)
