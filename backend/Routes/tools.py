from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from backend.models import users, Ind_Profile
import requests


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


@api_view(['POST'])
def get_github_repo_details(request):
    owner = request.data.get('owner')
    repo  = request.data.get('repo')
    
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    if response.status_code == 200:
        repo_data = response.json()
        is_forked = repo_data['fork']
        project_details = {
            'name': repo_data['name'],
            'description': repo_data['description'],
            'forked': is_forked,
            'forked_from': repo_data['parent']['full_name'] if is_forked else None,
            'url': repo_data['html_url'],
            # Add more fields as needed
        }
        return project_details
    else:
        return None