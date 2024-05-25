# Django imports

# Rest Framework imports
from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    )

# Local imports
from .models import Todo

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

