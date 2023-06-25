import requests

def refresh_access_token():
    # Endpoint to refresh the access token
    refresh_url = 'https://oauth2.googleapis.com/token'

    refresh_data = {
        'client_id': '738289713788-oaob3rgnc39pt2sa2d3gcs7hv36vua9c.apps.googleusercontent.com',
        'client_secret': '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',
        'refresh_token': "1//04vDWzDauNkaxCgYIARAAGAQSNwF-L9IrbyaVngBdgOS-e2VlAXb1B3QpTZUQy8ywMjCBoEDMuPtXipTjhULtV9p_tFrwdbtak8g",
        'grant_type': 'refresh_token'
    }

    # Send the request to refresh the access token
    response = requests.post(refresh_url, data=refresh_data)
    if response.status_code == 200:
        # Extract the new access token from the response
        access_token = response.json().get('access_token')
        return access_token
    else:
        print('Error occurred while refreshing the access token:', response.text)
        return None
refresh_access_token()