import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials

folder_id = '1xenMtBaq7Gww4TayFftQGhHAPBksA2oZ'

credentials = Credentials.from_service_account_file('./client_secrets.json', scopes=['https://www.googleapis.com/auth/drive.file'])

service = build('drive', 'v3', credentials=credentials)

def upload_image(file_path, folder_id):
    file_name = os.path.basename(file_path)
    
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }

    media = MediaFileUpload(file_path, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    print(f'File ID: {file.get("id")}, File Name: {file_name} uploaded to folder ID: {folder_id}')

image_folder_path = './data/'

for filename in os.listdir(image_folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'): 
        file_path = os.path.join(image_folder_path, filename)
        upload_image(file_path, folder_id)
