import requests
import json

def upload_image_to_drive():
    upload_url = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart'
    metadata_url = 'https://www.googleapis.com/drive/v3/files'

    headers = {
        "Authorization": "Bearer ya29.a0AWY7CklWLbi1MIIyz7Jm5Q-pofUP9f91HaHpYUiZnP46GslROg95iqmiHWQtCaXZfOSPScjCB3eGtQXT5iYm9LkD77oRBQca_Z1ZSImUULDUf5156zu_ixFJtcbjooBu2ejLFdTcVQBE7MWHjrLXJ6d051CGaCgYKAZQSARMSFQG1tDrpyrg7y-_8wzQ9EgZxl7h_Hw0163"
    }

    metadata = {
        'name': 'Final (1).pdf'
    }
 
    files = {
        'metadata': ('metadata', json.dumps(metadata), 'application/json; charset=UTF-8'),
        'file': open("C:/Users/nagip/Downloads/Final (1).pdf", 'rb')
    }

    # Upload the file
    response = requests.post(upload_url, headers=headers, files=files)
    if response.status_code == 200:
        file_id = response.json().get('id')
        print('Image uploaded successfully.')
    else:
        print('Error occurred while uploading the image:', response.text)
        return

    # Get the shareable link
    shareable_link_url = f'{metadata_url}/{file_id}?fields=webViewLink'
    response = requests.get(shareable_link_url, headers=headers)
    if response.status_code == 200:
        webViewLink = response.json().get('webViewLink')
        print('Shareable link:', webViewLink)
    else:
        print('Error occurred while obtaining the shareable link:', response.text)
        return

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


upload_image_to_drive()
