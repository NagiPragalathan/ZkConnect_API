from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.models import Ind_Profile

@api_view(['POST'])
def profile_data(request):
    
    # Create a new instance of Ind_Profile with the provided data
    profile = Ind_Profile(
        id=len(Ind_Profile.objects.all())+1,
        first_name=request.data.get('first_name'),
        last_name=request.data.get('last_name'),
        profile_bio=request.data.get('profile_bio', 'the bio not filled yet.'),
        contact_number=request.data.get('contact_number'),
        location=request.data.get('location'),
        skills=request.data.get('skills'),
        resume_image=request.data.get('resume_image'),
        usr_type=request.data.get('usr_type')
    )
    
    # Save the profile instance to the database
    profile.save()
    
    return Response({'success': True, 'message': 'Data stored successfully.'})
