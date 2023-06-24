from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get_user_data(request):
    user = request.user
    if user.is_authenticated:
        # Retrieve the user's data
        username = user.username
        email = user.email
        # ... additional fields

        # Return the user's data
        data = {
            'username': username,
            'email': email,
            # ... additional fields
        }
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'User not authenticated.'}, status=status.HTTP_401_UNAUTHORIZED)
