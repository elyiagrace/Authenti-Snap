# screenshot_processor.py

import requests  # Used for making API calls to Pinata
from PIL import ImageGrab
import hashlib
import os
from datetime import datetime
import json
from browser_url import get_current_url

# Pinata API credentials (replace with your own)
PINATA_API_KEY = 'YOUR PINATA KEY'
PINATA_SECRET_API_KEY = 'YOUR PINATA SECRET API KEY'

class ScreenshotProcessor:
    def __init__(self, file_path="snip_screenshot.png"):
        self.file_path = file_path
        self.current_url = get_current_url()

    def save_screenshot(self, bbox):
        """ Capture and save the screenshot within the selected bounding box. """
        screenshot = ImageGrab.grab(bbox=bbox)  # Use PIL to grab the image
        screenshot.save(self.file_path)
        print(f"Screenshot saved to {self.file_path}")
        return self.file_path


    def hash_screenshot(self):
        """ Generate a SHA-256 hash of the screenshot including URL and date-time. """
        try:
            # Retrieve the current URL
            if not self.current_url:
                raise Exception("Failed to retrieve the current URL")

            # Get the current date and time
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.file_path, "rb") as f:
                file_bytes = f.read()

            # Concatenate file bytes, URL, and date-time
            combined_data = file_bytes + current_datetime.encode() + str(self.current_url).encode()

            # Generate the SHA-256 hash
            file_hash = hashlib.sha256(combined_data).hexdigest()
            print(f"Screenshot Hash: {file_hash}")
            return file_hash
        except Exception as e:
            print(f"An error occurred while hashing the screenshot: {e}")
            return None

    def store_to_ipfs(self):
        """ Upload the screenshot to Pinata (IPFS) with date-time metadata. """
        url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

        # Get the current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Metadata to attach to the file
        pinata_metadata = {
            "name": os.path.basename(self.file_path),  # File name as the metadata name
            "keyvalues": {
                "date_time": current_datetime,  # Custom metadata field for date and time
                "url": str(self.current_url)
            }
        }

        # Open the image file to send it in the request
        with open(self.file_path, 'rb') as file:
            files = {
                'file': (os.path.basename(self.file_path), file)
            }
            headers = {
                'pinata_api_key': PINATA_API_KEY,
                'pinata_secret_api_key': PINATA_SECRET_API_KEY
            }

            # Send POST request with metadata and file
            response = requests.post(url, files=files, headers=headers, data={
                'pinataMetadata': json.dumps(pinata_metadata)
            })

        if response.status_code == 200:
            ipfs_hash = response.json()['IpfsHash']
            print(f"File uploaded to IPFS with metadata. IPFS Hash: {ipfs_hash}")
            return ipfs_hash
        else:
            print(f"Failed to upload file with metadata: {response.status_code} {response.text}")
            return None
