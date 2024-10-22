from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Reminder
from .services import openai_service


chatgpt_service = openai_service.ChatGPTService()
openai_service.ChatGPTService

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
 
class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('id', 'event', 'description', 'location')