import jwt
from datetime import datetime, timedelta
from django.conf import settings

def generate_jwt_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=1),  # Token expira em 1 hora
        'iat': datetime.utcnow(),  # Token emitido agora
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
