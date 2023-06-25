import requests

# Define the URL of your Django REST Framework endpoint
url = 'http://localhost:8000/upload_img_file/'

# Create a dictionary representing the file you want to upload
file_data = {
    'file': open("C:/Users/nagip/Downloads/Final (1).pdf", 'rb')
}

# Send a POST request to upload the file
response = requests.post(url, files=file_data)

# Print the response from the server
print(response.json())

{
        "id":" id",
        "firstName":" firstName",
        "lastName":" lastName",
        "email":" email",
        "location":" location",
        "contactNumber":" contactNumber",
        "profileBio":" profileBio",
        "file":" resume",
        "file_name":" resume.name",
        "type":" selectedButton",
        "skills":" selectedSkil",
      }