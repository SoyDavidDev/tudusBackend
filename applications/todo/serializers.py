# Rest Framework imports
from rest_framework import serializers

# Local imports
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

