from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import User
import string
import random
from rest_framework_simplejwt.tokens import RefreshToken

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['username'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
def create(request):
    try:
        email = request.data.get('email', None)
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        confirmpassword = request.data.get('confirmpassword', None)
        print(email, username, password, confirmpassword)

        if email and User.objects.filter(email=email).exists():
            return Response({"res": "Email already exists"}, status=409)  # Conflict
        if username and User.objects.filter(username=username).exists():
            return Response({"res": "Username already exists"}, status=409)  # Conflict
        if len(username) > 30:
            return Response({"res": "Username must not be greater than 30 characters"}, status=400)  # Bad Request
        if password != confirmpassword:
            return Response({'res': "Passwords don't match"}, status=400)  # Bad Request
        
        user = User.objects.create_user(email=email, username=username, password=password)
        user.auth_token = generate_random_string()
        user.password_auth = ""
        user.save()
        return Response({'res': 'Success'}, status=201)  # Created
    except Exception as e:
        return Response({'res': f'Error: {e}'}, status=500)  # Internal Server Error

    

def generate_random_string(length=30):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string