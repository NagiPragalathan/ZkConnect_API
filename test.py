import os
import requests
import json

def upload_image_to_drive():
    url = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart'

    headers = {
        'Authorization': "Bearer ya29.a0AWY7Ckna7Y_ehDdYfaeGA8_SzgPaSsOkkUHbGwfpUcvwyTaM4Z2U01qly6CtsLxW1NVOipKhZoQR1aR7uUDwAtgbSaSBT_H64Afwb77y23K653PB5MqHu_rVc9sEF6zS0an0JTDG2EzDg9StMR7B8RG5XBqKaCgYKAQ0SARASFQG1tDrpF4H9mLrZrqKjntXp-7rxWw0163"
    }

    params = {
        'name': 'samplefile.jpg',
        'permissions': [{'role': 'reader', 'type': 'anyone'}]
    }

    files = {
        'data': ('metadata', json.dumps(params), 'application/json; charset=UTF-8'),
        'file': open("C:/Users/nagip/OneDrive/Pictures/download.jpg", 'rb')
    }

    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        file_data = response.json()
        file_id = file_data.get('id')
        download_link = f'https://drive.google.com/uc?export=download&id={file_id}'
        print('Image uploaded successfully.')
        print('Download link:', download_link)
        return download_link
    else:
        print('Error occurred while uploading the image:', response.text)
        return None

# Example usage
download_link = upload_image_to_drive()

# Download the uploaded image
if download_link:
    output_path = 'path/to/downloaded_image.jpg'
    response = requests.get(download_link)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print('Image downloaded successfully.')
    else:
        print('Error occurred while downloading the image:', response.text)
