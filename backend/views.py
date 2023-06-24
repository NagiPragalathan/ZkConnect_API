from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import users
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout

@api_view()
def home(request):
    return Response({
        'status' : 200,
        'message' : 'Yes! Django rest FrameWork is Working !!!'
    })
    
@api_view(['POST','PATCH'])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    role = request.data.get('role')
    # user = User.objects.create_user(username=username, email=email, password=password)
    # print("User created with username:", username)
    obj = users(userid=22, username=username, email=email, password=password, role=role)
    obj.save()
    print("User details saved in the database")
    return Response({'Success': 'User Created'}, status=status.HTTP_201_CREATED)
   

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if username and password:
        if user is not None:
            login(request, user)
            # Redirect to a success page or any other desired action
            return Response({'Susses': 'Invalid username or password.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'error': 'Missing required fields.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
def logout_view(request):
    logout(request)
    # Redirect to a desired page after logging out
    return redirect('home')


def welcome_home(request):
    return render(request,'welcome_page.html')