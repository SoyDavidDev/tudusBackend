# Rest Framework imports
from rest_framework import serializers

# Local imports
from .models import Todo
from applications.user.models import User
from applications.lists.models import List

class TodoSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    list_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'user_id', 'list_id']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        list_id = validated_data.pop('list_id')
        user = User.objects.get(id=user_id)
        list = List.objects.get(id=list_id)
        todo = Todo.objects.create(user_id=user, list_id=list, **validated_data)
        return todo
    


