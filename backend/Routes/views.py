from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import users

from django.contrib.auth import authenticate, login
from django.contrib.sessions.backends.db import SessionStore
from django.middleware.csrf import rotate_token
from rest_framework.decorators import permission_classes



@api_view()
def home(request):
    return Response({
        'status' : 200,
        'message' : 'Yes! Django rest FrameWork is Working !!!'
    })

@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    role = request.data.get('role')
    if username and password and email:
        try:
            print(f"The {username} are user creation started")
            print(username,password,email,role)
            user = User.objects.create_user(username=username, password=password, email=email)
            print("will print")
            print(user.id)
            obj = users(userid=user.id,username=username,email=email,password=password,role=role)
            obj.save()
            print("user created")
            return Response({'Susses': 'User Created'},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': 'Unable to create user.'+str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Missing required fields.'}, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def login_fn(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username and password:
        user = authenticate(request._request, username=username, password=password)
        if user is not None:
            # Create a new session
            session = SessionStore()
            session['user_id'] = user.id
            session.create()

            # Rotate the CSRF token to prevent potential CSRF attacks
            rotate_token(request._request)

            # Login the user
            login(request._request, user)

            return Response({'success': 'Login successful.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'error': 'Missing required fields.'}, status=status.HTTP_400_BAD_REQUEST)

def welcome_home(request):
    return render(request,'welcome_page.html')