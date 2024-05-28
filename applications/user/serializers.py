# Rest framework imports
from rest_framework import serializers

# Local imports
from .models import User


# Our UserSerializer class organizes to render into JSON or XML format.
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = User
        fields = ['id', 'username','password', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
    
    def create(self, validated_data):
        validated_data['is_active'] = True
        user = User.objects.create_user(**validated_data)
        return user
