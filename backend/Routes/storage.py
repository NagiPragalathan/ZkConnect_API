import requests
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view
import os


@api_view(['POST'])
def upload_file(request):
    try:
        uploaded_file = request.FILES.get('file')  # Retrieve the uploaded file
        print(uploaded_file)
        filename = request.data.get('file_name')
        # Process or save the file as needed
        # Replace this with your own logic to handle file processing or storage

        # Upload the file to Google Drive
        upload_url = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart'
        metadata_url = 'https://www.googleapis.com/drive/v3/files'

        headers = {
            "Authorization": "Bearer ya29.a0AWY7CkmK67PbjEnnSW8o7OfhVB2OJxoe-h0atv68m_z1ub5qGM93G-8wXxB0hhmm_Ntf-_TayFfOZXWPAbz495yb5d3DAu0Lev5bxFa9iW66N_Eqwd-2ARNH4Q_g2u9M5KrZ2sEdTi_us2ouLEddHUKU_5IeaCgYKAQESARESFQG1tDrpFKbkBLTPbgwuMfVsfxRt0w0163",
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

        return Response({'message': 'File uploaded successfully', 'webViewLink': webViewLink})
    except Exception as e:
        return Response({'error': str(e)}, status=500)
