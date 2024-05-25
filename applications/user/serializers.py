# Rest framework imports
from rest_framework import serializers

# Local imports
from .models import User


# Our UserSerializer class organizes to render into JSON or XML format.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
