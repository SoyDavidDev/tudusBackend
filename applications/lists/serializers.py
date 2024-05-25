# Rest framework imports
from rest_framework import serializers

# Local imports
from .models import List
from applications.todo.serializers import TodoSerializer

# Our ListSerializer class organizes to render into JSON or XML format.
class ListSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)
    
    class Meta:
        model = List
        fields = '__all__'

