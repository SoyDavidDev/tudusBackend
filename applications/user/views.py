# Python imports
import jwt

# Django imports
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError as DjangoValidationError
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.sessions.models import Session
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings

# Rest Framework imports
from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    )
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework import serializers
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken


# Local imports
from .models import User
from applications.lists.models import List
from src.settings.base import EMAIL_HOST_USER

# Serializers
from .serializers import UserSerializer, ChangePasswordSerializer, PasswordResetSerializer
from applications.lists.serializers import ListSerializer


class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserLists(ListAPIView):
    serializer_class = ListSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']

        user = get_object_or_404(User, id=user_id)
        return user.lists.all()


class CreateUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
class UserDetail(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDelete(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserUpdate(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # Todos los queryset son las referencias a la base de datos

# UserRetrieveUpdate también permitirá operaciones de lectura (GET)
class UserRetrieveUpdate(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['id'] = user.id

        return token
    
    def validate(self, attrs):
        try:
            self.user = User.objects.get(username=attrs['username'])
        except User.DoesNotExist:
            raise AuthenticationFailed('No se ha encontrado un usuario con ese nombre de usuario')
        

        if not self.user.check_password(attrs['password']):
            raise AuthenticationFailed('Contraseña incorrecta')
        
        was_inactive = False
        if not self.user.is_active:
            self.user.is_active = True
            self.user.save()
            was_inactive = True
                    
        
        data = {}
        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['id'] = self.user.id
        data['was_inactive'] = was_inactive

        if api_settings.UPDATE_LAST_LOGIN:
            self.user.last_login = timezone.now()
            self.user.save(update_fields=['last_login'])

        return data



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer


class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.data.get('old_password')
            if not request.user.check_password(old_password):
                return Response({'old_password': 'Contraseña incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
            request.user.set_password(serializer.data.get('new_password'))
            request.user.save()
            return Response({'message': 'Contraseña actualizada correctamente'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PauseAccountView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['pk'])

        if request.user != user:
            return Response({'message': 'No tienes permiso para pausar esta cuenta'}, 
                            status=status.HTTP_401_UNAUTHORIZED)
        
        user.is_active = False
        user.save()

        Session.objects.filter(user=user).delete()
        
        return Response({'message': 'Cuenta pausada correctamente'}, status=status.HTTP_200_OK)


class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        print (user)

        if user is None:
            return Response({'message': 'No se ha encontrado un usuario con ese correo electrónico'}, 
                            status=status.HTTP_404_NOT_FOUND)
        refresh = RefreshToken.for_user(user)
        token = str(refresh)

        reset_url = reverse('reset-password-confirm')
        absolute_url = f'http://localhost:8000{reset_url}?token={token}'
        email_body = f'Usa este enlace para restablecer tu contraseña\n{absolute_url}'
        data = {
            'email_body': email_body,
            'to_email': user.email,
            'email_subject': 'Restablecer contraseña'
        }
        send_mail(
            data['email_subject'],
            data['email_body'],
            settings.EMAIL_HOST_USER,
            [data['to_email']],
            fail_silently=False
        )
        return Response({'message': 'Se ha enviado un enlace para restablecer la contraseña al correo electrónico proporcionado'}, 
                        status=status.HTTP_200_OK)

class PasswordResetConfirmView(APIView):
    def post(self,request):
        token = request.data.get('token')
        password = request.data.get('password')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            user.set_password(password)
            user.save()
        except Exception as e:
            return Response({'error': 'El token no es válido, por favor solicita un nuevo enlace para restablecer la contraseña'}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message': 'Contraseña restablecida correctamente'}, 
                        status=status.HTTP_200_OK)


