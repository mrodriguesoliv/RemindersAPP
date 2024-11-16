from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Reminder
from core.services import openai_service


chatgpt_service = openai_service.ChatGPTService()
openai_service.ChatGPTService
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if not password:
            raise serializers.ValidationError({'password': 'A senha é obrigatória.'})

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
 
class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('id', 'event', 'description', 'location')