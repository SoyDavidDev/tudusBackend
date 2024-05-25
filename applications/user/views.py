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
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Local imports
from .models import User
from applications.lists.models import List
# Serializers
from .serializers import UserSerializer
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