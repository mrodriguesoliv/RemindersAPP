import requests
from django.conf import settings
import os
from dotenv import load_dotenv
import re
from datetime import datetime
from core.models import Reminder
import re
import json
from openai.types.chat.completion_create_params import ResponseFormat

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

class ChatGPTService:
    def __init__(self):
        self.api_key = OPENAI_API_KEY
        self.api_url = 'https://api.openai.com/v1/chat/completions'

        print(f'teste: {OPENAI_API_KEY}')
        

    def get_response(self,conversation_id, message=None, max_tokens=150):

        from core.models import Interaction

        interactions = Interaction.objects.filter(conversation_id=conversation_id).order_by('created_at')

        messages = [
            {'role': 'user', 'content': interaction.prompt} for interaction in interactions
        ]
        
        
        messages.append({'role': 'user', 'content': message})

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json', 
            
        }
        data = {
            'model': 'gpt-4-turbo',
            'messages': messages,
            'max_tokens': max_tokens,
            'temperature': 0.7, 
            'response_format': { "type":"json_object" },
        }

        response = requests.post(self.api_url, headers=headers, json=data)
        response_data = response.json()
        

        choices = response_data.get('choices', [])
        if choices:
            message_content = choices[0].get('message', {}).get('content', '')
            return message_content.strip() 
        
        return ''
    
    

    def get_response_detail(self,conversation_id, message=None, max_tokens=150):

        from core.models import Interaction

        interactions = Interaction.objects.filter(conversation_id=conversation_id).order_by('created_at')

        messages = [
            {'role': 'user', 'content': interaction.prompt} for interaction in interactions
        ]
        
        
        messages.append({'role': 'user', 'content': message})

        headers = {
            'Authorization': f'Bearer {self.api_key}', 
            
        }
        data = {
            'model': 'gpt-4-turbo',
            'messages': messages,
            'max_tokens': max_tokens,
            'temperature': 0.7,
        }

        response = requests.post(self.api_url, headers=headers, json=data)
        response_data = response.json()
        

        choices = response_data.get('choices', [])
        if choices:
            message_content = choices[0].get('message', {}).get('content', '')
            return message_content.strip() 
        
        return ''
        
    