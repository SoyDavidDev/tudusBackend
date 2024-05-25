# Rest framework imports
from rest_framework import serializers

# Local imports
from .models import User


# Our UserSerializer class organizes to render into JSON or XML format.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
