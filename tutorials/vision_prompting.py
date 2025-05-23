from anthropic import Anthropic
from dotenv import load_dotenv

from IPython.display import Image
import mimetypes

import base64

load_dotenv()
client = Anthropic()

Image(filename='./images/people.png') 

def create_image_message(image_path):
    # Open the image file in "read binary" mode
    with open(image_path, "rb") as image_file:
        # Read the contents of the image as a bytes object
        binary_data = image_file.read()
    
    # Encode the binary data using Base64 encoding
    base64_encoded_data = base64.b64encode(binary_data)
    
    # Decode base64_encoded_data from bytes to a string
    base64_string = base64_encoded_data.decode('utf-8')
    
    # Get the MIME type of the image based on its file extension
    mime_type, _ = mimetypes.guess_type(image_path)
    
    # Create the image block
    image_block = {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": mime_type,
            "data": base64_string
        }
    }
    
    return image_block

messages=[
    {
        "role": "user", 
        "content": [
            create_image_message('./images/people.png'),
            {
                "type": "text",
                "text": "how many people are in this image?"
            }
        ],
    }
]

response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2048,
    messages=messages
)

print(response.content[0].text)