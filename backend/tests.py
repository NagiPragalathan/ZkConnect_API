# from django.test import TestCase

# Create your tests here.

# Models Details

# Ind_Profile which is contain [first_name, Last_name, Profile_bio, skills, Resume_image
# write the django models code for SocialLinks which is contains [ id, userid, github, linkedin, twitter]
# write the django models code for Rec_Profile which is contain [first_name, Last_name, Profile_bio, company_name, description, logo]

# write the django models code for Skills which is contains [ id, Name, type-default:tech]

# write the django models code for CompanyDetails which is contains [id, company_name, company_bio, start_year,no_of_emp, SocialLinks, logo]

# write the django models code for JobCreate which is contains [id, CompanyDetails, description, experience, looking_for, sallery, environment ]

# write the django models code for StackReq which is contains [ stackid, JobCreateid, Skills ]

# write the django models code for Applyed_jobs which is contains [id, userid, JobCreateid, status]


'''
reference.......

import React, { useState } from 'react';
import axios from 'axios';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/login/', { username, password });
      console.log(response.data); // Handle the success response
    } catch (error) {
      console.error(error.response.data); // Handle the error response
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Username:
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
        </label>
        <br />
        <label>
          Password:
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </label>
        <br />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;

'''

a={
  "access_token": "ya29.a0AWY7Ckna7Y_ehDdYfaeGA8_SzgPaSsOkkUHbGwfpUcvwyTaM4Z2U01qly6CtsLxW1NVOipKhZoQR1aR7uUDwAtgbSaSBT_H64Afwb77y23K653PB5MqHu_rVc9sEF6zS0an0JTDG2EzDg9StMR7B8RG5XBqKaCgYKAQ0SARASFQG1tDrpF4H9mLrZrqKjntXp-7rxWw0163", 
  "scope": "https://www.googleapis.com/auth/drive", 
  "token_type": "Bearer", 
  "expires_in": 3599, 
  "refresh_token": "1//04CTHHaBk08vMCgYIARAAGAQSNwF-L9IrOP2Ds7VRIRNCH0mPLB90EuCcmuha8meGc24DabR7gCea83XHGFw2t_P8tJWoZ2Ip5qo"
}

import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
import json
a={
    "Authorization" : "Bearer ya29.a0AWY7Ckna7Y_ehDdYfaeGA8_SzgPaSsOkkUHbGwfpUcvwyTaM4Z2U01qly6CtsLxW1NVOipKhZoQR1aR7uUDwAtgbSaSBT_H64Afwb77y23K653PB5MqHu_rVc9sEF6zS0an0JTDG2EzDg9StMR7B8RG5XBqKaCgYKAQ0SARASFQG1tDrpF4H9mLrZrqKjntXp-7rxWw0163"
 }


import os
import requests

def upload_image_to_drive():
    url = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart'

    headers = {
        'Authorization': "Bearer ya29.a0AWY7Ckna7Y_ehDdYfaeGA8_SzgPaSsOkkUHbGwfpUcvwyTaM4Z2U01qly6CtsLxW1NVOipKhZoQR1aR7uUDwAtgbSaSBT_H64Afwb77y23K653PB5MqHu_rVc9sEF6zS0an0JTDG2EzDg9StMR7B8RG5XBqKaCgYKAQ0SARASFQG1tDrpF4H9mLrZrqKjntXp-7rxWw0163"
    }

    params = {
        'name': 'samplefile.jpg',
    }
  
    files = {
        'data': ('metadata', json.dumps(params), 'application/json; charset=UTF-8'),
        'file': open("C:/Users/nagip/OneDrive/Pictures/download.jpg", 'rb')
    }

    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        print('Image uploaded successfully.')
    else:
        print('Error occurred while uploading the image:', response.text)

# Example usage
image_path = 'path/to/image.jpg'
folder_id = 'your_folder_id'  # ID of the destination folder in Google Drive
access_token = 'your_access_token'  # Access token with required permissions

upload_image_to_drive()


def download_image_from_drive(file_id, output_path):
    url = f'https://www.googleapis.com/drive/v3/files/{file_id}?alt=media'

    headers = {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print('Image downloaded successfully.')
    else:
        print('Error occurred while downloading the image:', response.text)