# usuarios/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer, LoginSerializer, DisenadorSerializer, TipoPrendaSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from .models import Disenador, TipoPrenda
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
import base64


class ExportDesignsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        designs_ids = request.data.get("designs", [])
        recipient_email = request.data.get("email", "")

        if not recipient_email:
            return Response({"error": "Correo del destinatario es requerido."}, status=400)

        designs = Disenador.objects.filter(id__in=designs_ids, usuario=request.user)
        if not designs.exists():
            return Response({"error": "No se encontraron diseños válidos."}, status=404)

        # Generar el contenido del correo
        message = "Aquí están los diseños que seleccionaste:\n"
        for design in designs:
            message += f"- {design.tipo_prenda}: {request.build_absolute_uri(design.imagen.url)}\n"

        # Enviar el correo
        email = EmailMessage(
            subject="Tus diseños compartidos",
            body=message,
            to=[recipient_email],
        )
        email.send()

        return Response({"message": "Diseños enviados exitosamente."})

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
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SaveDesignView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user  # Usuario autenticado
        print(f"Usuario autenticado: {user}")  # Depuración

        # Validar tipo de prenda
        tipo_prenda_nombre = request.data.get("tipo_prenda")
        try:
            tipo_prenda = TipoPrenda.objects.get(nombre=tipo_prenda_nombre)
        except TipoPrenda.DoesNotExist:
            return Response({"error": "Tipo de prenda no válido"}, status=status.HTTP_400_BAD_REQUEST)

        # Procesar la imagen
        imagen_base64 = request.data.get("imagen")
        if not imagen_base64:
            return Response({"error": "La imagen es requerida"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            format, imgstr = imagen_base64.split(';base64,')
            ext = format.split('/')[-1]
            imagen = ContentFile(base64.b64decode(imgstr), name=f'diseno_{user.id}.{ext}')
        except Exception as e:
            return Response({"error": f"Error al procesar la imagen: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        # Crear el diseño
        disenador = Disenador.objects.create(
            usuario=user,
            tipo_prenda=tipo_prenda,
            imagen=imagen
        )

        return Response({
            "message": "Diseño creado exitosamente",
            "disenador": {
                "id": disenador.id,
                "tipo_prenda": disenador.tipo_prenda.nombre,
                "imagen": disenador.imagen.url,
            }
        }, status=status.HTTP_201_CREATED)


class DesignListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(f"Usuario autenticado: {request.user}")  # Para depuración
        designs = Disenador.objects.filter(usuario=request.user)  # Filtra por el usuario autenticado
        serializer = DisenadorSerializer(designs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class DesignCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user  # Usuario autenticado

        # Validar tipo de prenda
        tipo_prenda_nombre = request.data.get("tipo_prenda")
        try:
            tipo_prenda = TipoPrenda.objects.get(nombre=tipo_prenda_nombre)
        except TipoPrenda.DoesNotExist:
            return Response({"error": "Tipo de prenda no válido"}, status=status.HTTP_400_BAD_REQUEST)

        # Procesar la imagen en base64
        imagen_base64 = request.data.get("imagen")
        if not imagen_base64:
            return Response({"error": "La imagen es requerida"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            format, imgstr = imagen_base64.split(";base64,")
            ext = format.split("/")[-1]
            imagen = ContentFile(base64.b64decode(imgstr), name=f'diseno_{user.id}.{ext}')
        except Exception as e:
            return Response({"error": f"Error al procesar la imagen: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        # Crear diseño
        disenador = Disenador.objects.create(
            usuario=user,
            tipo_prenda=tipo_prenda,
            imagen=imagen
        )

        return Response({
            "message": "Diseño creado exitosamente",
            "disenador": {
                "id": disenador.id,
                "tipo_prenda": disenador.tipo_prenda.nombre,
                "imagen": disenador.imagen.url,
            }
        }, status=status.HTTP_201_CREATED)


class DesignDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        user = request.user
        design = get_object_or_404(Disenador, id=pk, usuario=user)
        design.delete()
        return Response({'detail': 'Diseño eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)


class TipoPrendaListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tipos_prenda = TipoPrenda.objects.all()
        serializer = TipoPrendaSerializer(tipos_prenda, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
