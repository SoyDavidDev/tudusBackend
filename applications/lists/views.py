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

# Local imports
from .models import List
from applications.todo.models import Todo
from applications.user.models import User

# Serializers
from .serializers import ListSerializer
from applications.todo.serializers import TodoSerializer    


class ListList(ListAPIView):
    serializer_class = ListSerializer
    queryset = List.objects.all()

class ListTodos(ListAPIView):
    serializer_class = TodoSerializer
    
    def get_queryset(self):
        list_id = self.kwargs['pk']
        # We manage the exception here to return a 404 response
        list = get_object_or_404(List, id=list_id)
        return list.todos.all()
 

class CreateList(CreateAPIView):
    serializer_class = ListSerializer
    queryset = List.objects.all()

class CreateListbyUser(CreateAPIView):
    serializer_class = ListSerializer
    queryset = List.objects.all()

    def perform_create(self, serializer):
        user_id = self.request.data.get('user_id')
        user = get_object_or_404(User, id=user_id)
        serializer.save(user=user)



class ListDetail(RetrieveAPIView):
    serializer_class = ListSerializer
    queryset = List.objects.all()

class ListDelete(DestroyAPIView):
    serializer_class = ListSerializer
    queryset = List.objects.all()

class ListUpdate(UpdateAPIView):
    serializer_class = ListSerializer
    queryset = List.objects.all()

class ListRetrieveUpdate(RetrieveUpdateAPIView):
    serializer_class = ListSerializer
    queryset = List.objects.all()
