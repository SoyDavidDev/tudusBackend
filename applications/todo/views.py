# Django imports
from django.core.exceptions import ObjectDoesNotExist
# Rest Framework imports
from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    )
from rest_framework.exceptions import ValidationError

# Local imports
from .models import Todo
from applications.lists.models import List

# Serializers
from .serializers import TodoSerializer

class TodoList(ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class TodoDetail(RetrieveAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class TodoDelete(DestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class TodoUpdate(UpdateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class TodoCreate(CreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class TodoRetrieveUpdate(RetrieveUpdateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

