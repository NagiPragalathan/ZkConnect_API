from rest_framework import serializers
from .models import users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'

from rest_framework import serializers

class CurrentUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    # Add other fields from the user model as needed