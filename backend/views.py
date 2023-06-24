from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def home(request):
    return Response({
        'status' : 200,
        'message' : 'Yes! Django rest FrameWork is Working !!!'
    })
    
    
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if username and password and email:
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response({'error': 'Unable to create user.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Missing required fields.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username and password:
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            # Perform any additional operations or authentication checks here if needed
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'error': 'Missing required fields.'}, status=status.HTTP_400_BAD_REQUEST)
