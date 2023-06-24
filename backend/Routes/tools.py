from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from backend.serializers import CurrentUserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user_data(request):
    serializer = CurrentUserSerializer(request.user)
    return Response(serializer.data)


# @api_view(['GET'])
# def get_user_data(request):
#     user = request.user
#     if user.is_authenticated:
#         # Retrieve the user's data
#         username = user.username
#         email = user.email
#         # ... additional fields

#         # Return the user's data
#         data = {
#             'username': username,
#             'email': email,
#             # ... additional fields
#         }
#         return Response(data, status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'User not authenticated.'}, status=status.HTTP_401_UNAUTHORIZED)
