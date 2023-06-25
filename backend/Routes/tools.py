from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from backend.models import users, Ind_Profile

@api_view(['POST'])
def get_profile_data(request):
    usrid = request.data.get('id')
    try:
        profile = Ind_Profile.objects.get(userid=usrid)
        data = {
            'id': profile.id,
            'userid': profile.userid,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'profile_bio': profile.profile_bio,
            'contact_number': profile.contact_number,
            'location': profile.location,
            'skills': profile.skills,
            'resume_image': profile.resume_image,
            'usr_type': profile.usr_type,
        }
        return Response(data)
    except Ind_Profile.DoesNotExist:
        return Response({'error': 'Profile not found.'}, status=404)