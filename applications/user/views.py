# Django imports
from django.shortcuts import get_object_or_404
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
from rest_framework.decorators import api_view

# Local imports
from .models import User
from applications.lists.models import List
# Serializers
from .serializers import UserSerializer, ChangePasswordSerializer
from applications.lists.serializers import ListSerializer


class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserLists(ListAPIView):
    serializer_class = ListSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        # We manage the exception here to return a 404 response
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

        # Add custom claims
        token['id'] = user.id

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data['id'] = self.user.id

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
            return Response({'message': 'No tienes permiso para pausar esta cuenta'}, status=status.HTTP_401_UNAUTHORIZED)
        
        user.is_active = False
        user.save()
        return Response({'message': 'Cuenta pausada correctamente'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def activate_user(request,username):
    try:
        user = User.objects.get(username=username)
        user.is_active = True
        user.save()
        return Response({'message': 'Cuenta activada correctamente'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'message': 'El usuario no existe'}, status=status.HTTP_404_NOT_FOUND)





