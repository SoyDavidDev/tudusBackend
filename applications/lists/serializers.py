# Rest framework imports
from rest_framework import serializers

# Local imports
from .models import List

# Our ListSerializer class organizes to render into JSON or XML format.
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'

