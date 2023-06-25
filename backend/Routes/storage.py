import requests
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view
import os

from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend.models import PDF
from backend.serializers import PDFSerializer

tocken="ya29.a0AWY7CkmeJ1NX7zZLPRVPmaCtwcpLZQ1bgjSV-1wF8QttIt12d2dnl570XzNALxKJjD8n2f52hVhurCOMEb6D09gVMcKa4oX3LaOi_U_4EmU1d3Er61H-KUFQydUeactvsx30ReLFgb0B1xM1sOIc9TuRnPVSYXgaCgYKAYgSARASFQG1tDrpbzUfObZv0-r8ScaUx2k7kg0166"

@api_view(['POST'])
def store_pdf(request):
    if request.method == 'POST':
        name = request.data.get('name')
        data = request.FILES.get('file').read()
        pdf = PDF(name=name, data=data)
        pdf.save()
        return Response('PDF stored successfully')

@api_view(['POST'])
def retrieve_pdf(request):
    try:
        name = request.data.get('name')
        pdf = PDF.objects.get(name=name)
        serializer = PDFSerializer(pdf)
        return Response(serializer.data)
    except PDF.DoesNotExist:
        return Response('PDF not found', status=404)


@api_view(['POST'])
def upload_file(request):
    upload_url = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart'
    metadata_url = 'https://www.googleapis.com/drive/v3/files'
    uploaded_file = request.FILES.get('file')  # Retrieve the uploaded file
    print(uploaded_file)
    filename = request.data.get('file_name')
    headers = {
        "Authorization": "Bearer "+tocken
    }

    metadata = {
        'name': filename
    }

    files = {
        'metadata': ('metadata', json.dumps(metadata), 'application/json; charset=UTF-8'),
        'file': uploaded_file
    }

    # Upload the file
    response = requests.post(upload_url, headers=headers, files=files)
    if response.status_code == 200:
        file_id = response.json().get('id')
        print('Image uploaded successfully.')
    else:
        print('Error occurred while uploading the image:', response.text)
        return Response({'error': 'Error occurred while uploading the image'}, status=500)

    # Get the shareable link
    shareable_link_url = f'{metadata_url}/{file_id}?fields=webViewLink'
    response = requests.get(shareable_link_url, headers=headers)
    if response.status_code == 200:
        webViewLink = response.json().get('webViewLink')
        print('Shareable link:', webViewLink)
    else:
        print('Error occurred while obtaining the shareable link:', response.text)
        return Response({'error': 'Error occurred while obtaining the shareable link'}, status=500)

    # Update permissions to make the file accessible to anyone
    permissions_url = f'{metadata_url}/{file_id}/permissions'

    # Define the request payload to set the permission
    permission_data = {
        'role': 'reader',
        'type': 'anyone'
    }

    # Send the request to update permissions
    response = requests.post(permissions_url, headers=headers, json=permission_data)
    if response.status_code == 200:
        print('Permissions updated successfully.')
    else:
        print('Error occurred while updating permissions:', response.text)

    return Response({'message': 'Image uploaded successfully', 'webViewLink': webViewLink})


def upload_files_to_drive(uploaded_file, filename):
    upload_url = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart'
    metadata_url = 'https://www.googleapis.com/drive/v3/files'

    headers = {
         "Authorization": "Bearer "+tocken
    }

    metadata = {
        'name': filename
    }

    files = {
        'metadata': ('metadata', json.dumps(metadata), 'application/json; charset=UTF-8'),
        'file': uploaded_file
    }

    # Upload the file
    response = requests.post(upload_url, headers=headers, files=files)
    if response.status_code == 200:
        file_id = response.json().get('id')
        print('Image uploaded successfully.')
    else:
        print('Error occurred while uploading the image:', response.text)
        return {'error': 'Error occurred while uploading the image'}
  # jdjn vljef
    # Get the shareable link
    shareable_link_url = f'{metadata_url}/{file_id}?fields=webViewLink'
    response = requests.get(shareable_link_url, headers=headers)
    if response.status_code == 200:
        webViewLink = response.json().get('webViewLink')
        print('Shareable link:', webViewLink)
    else:
        print('Error occurred while obtaining the shareable link:', response.text)
        return {'error': 'Error occurred while obtaining the shareable link'}

    # Update permissions to make the file accessible to anyone
    permissions_url = f'{metadata_url}/{file_id}/permissions'

    # Define the request payload to set the permission
    permission_data = {
        'role': 'reader',
        'type': 'anyone'
    }

    # Send the request to update permissions
    response = requests.post(permissions_url, headers=headers, json=permission_data)
    if response.status_code == 200:
        print('Permissions updated successfully.')
    else:
        print('Error occurred while updating permissions:', response.text)

    return {'message': 'Image uploaded successfully', 'webViewLink': webViewLink}
