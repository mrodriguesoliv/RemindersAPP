from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, viewsets
from .serializer import UserSerializer, ReminderSerializer
from .models import Reminder, Conversation, Interaction
from rest_framework import views, status
from rest_framework.response import Response
from core.services import openai_service
from dotenv import load_dotenv
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse, HttpRequest
from oauth2_provider.views import TokenView
from rest_framework.decorators import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.views import APIView
from oauth2_provider.models import AccessToken, Application
from django.utils import timezone
from datetime import datetime, timedelta
from .utils import generate_jwt_token
import openai
from django.shortcuts import render
from uuid import uuid4
import re
from datetime import datetime
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from core.backend.models import Reminder 
from core.services.openai_service import ChatGPTService
import os
import core.services.openai_service
import json
import requests

from django.views import View

 

class CreateUserView(APIView):
    def post(self, request:Request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObtainJWTTokenView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            application = Application.objects.get(name='ALANREST')
            token = generate_jwt_token(user.id)
            access_token = AccessToken.objects.create(
                user=user,
                application=application,
                token=token,
                expires=timezone.now() + timedelta(hours=1)
            )

            return JsonResponse({'token': token})
        return JsonResponse({'error': 'Invalid credentials'}, status=401)


class ReminderViewSet(viewsets.ModelViewSet):
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        print(f"Meu Usuário na View ReminderViewSet: {self.request.user}")
        return Reminder.objects.filter(user=self.request.user)


class ChatGPTView(APIView):
    permission_classes = [IsAuthenticated] 
    parser_classes = [JSONParser]
    
    def post(self, request):
        message = request.data.get('message', 'content')
        conversation_id = request.data.get('conversation_id', None)
        user = request.user if request.user.is_authenticated else None

        
        print(f'Received message: {message}')
        print(f'Qual usuario?: {user}')
        print(f'Conversation ID: {conversation_id}')


    
        if not message:
            return Response({'error': 'Nenhuma pergunta enviada!'}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            if conversation_id:
                try:
                    conversation = Conversation.objects.get(conversation_id=conversation_id, user=user)
                    print(f'Conversation found: {conversation}')
                    print(f'User found testando: {user}')
                except Conversation.DoesNotExist:
                    return Response({'error': 'Conversation not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                conversation_id = str(uuid4())
                conversation = Conversation.objects.create(
                    user=user,
                    conversation_id=conversation_id
                )
                
            
            chatgpt_service = openai_service.ChatGPTService()
            response_text = chatgpt_service.get_response(conversation_id,message)
            print(f'Resposta do ChatGPTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa: {response_text}') 

            try:
                json_reminder = json.loads(response_text)
                event = json_reminder['Evento']
                description = json_reminder['Descrição']
                location = json_reminder['Local']
                
                print(f'Evento: {event}')
                print(f'Descrição: {description}')
                print(f'Local: {location}')

                if response_text is None or response_text.strip() == "":
                    return Response({'error': 'Resposta do ChatGPT é nula ou vazia'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        
                interaction = Interaction.objects.create(
                    conversation=conversation,
                    prompt=message,
                    response=response_text,
                    user=user
                )
                interaction.save()

                reminder = Reminder.objects.create(
                    event=event,
                    description=description,
                    location=location,
                    user=user
                )
                reminder.save()

            except json.JSONDecodeError:
                print(f'Erro ao decodificar JSON: {response_text}')  # Adicione esta linha
                return Response({'error': 'Resposta do ChatGPT não é um JSON válido.'}, status=status.HTTP_400_BAD_REQUEST)

            except KeyError as e:
                print(f'Chave não encontrada na resposta: {e}')
                return Response({'error': 'xDados do lembrete estão faltando.'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(f'Ocorreu um erro: {e}')
            return Response({'error': 'Erro interno ao processar a solicitação.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        

class ChatGPTViewDetail(APIView):
    permission_classes = [AllowAny] 
    parser_classes = [JSONParser]
    
    def post(self, request):
        message = request.data.get('message', '')
        conversation_id = request.data.get('conversation_id', None)
        user = request.user if request.user.is_authenticated else None

        
        print(f'Received message: {message}')
        print(f'Qual usuario?: {user}')
        print(f'Conversation ID: {conversation_id}')


    
        if not message:
            return Response({'error': 'Nenhuma pergunta enviada!'}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            if conversation_id:
                try:
                    conversation = Conversation.objects.get(conversation_id=conversation_id, user=user)
                    print(f'Conversation found: {conversation}')
                except Conversation.DoesNotExist:
                    return Response({'error': 'Conversation not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                conversation_id = str(uuid4())
                conversation = Conversation.objects.create(
                    user=user,
                    conversation_id=conversation_id
                )
                
            
            chatgpt_service = openai_service.ChatGPTService()
            response_text = chatgpt_service.get_response_detail(conversation_id,message)
    
            return Response({'response': response_text, 'conversation_id': conversation_id}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Erro ao processar a solicitação'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)