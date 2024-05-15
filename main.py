import os

import requests

imagePath = "test_image.png"
channelId = 0

headers = {"Authorization": "auth token goes here obviously"}

payload = {
    "files": [
        {
            "filename": "image.png",
            "file_size": os.path.getsize(imagePath),
        }
    ]
}

req = requests.post(
    f"https://discord.com/api/v9/channels/{channelId}/attachments",
    json=payload,
    headers=headers,
).json()

imageAttachment = req["attachments"][0]
uploadUrl = imageAttachment["upload_url"]
uploadFilename = imageAttachment["upload_filename"]

requests.put(uploadUrl, data=open(imagePath, "rb"))

payload = {
    "attachments": [
        {
            "id": "0",
            "filename": "image.png",
            "uploaded_filename": uploadFilename,
            "is_remix": True,
        }
    ]
}

req = requests.post(
    f"https://discord.com/api/v9/channels/{channelId}/messages",
    json=payload,
    headers=headers,
).text

print(req)
