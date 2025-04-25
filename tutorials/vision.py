from anthropic import Anthropic
from dotenv import load_dotenv

import base64

load_dotenv()
client = Anthropic()

with open("./images/uh_oh.png", "rb") as image_file:
    # binary_data = image_file.read()
    # base_64_encoded_data = base64.b64encode(binary_data)
    # base64_string = base_64_encoded_data.decode('utf-8')

    #reads the contents of the image as a bytes object
    binary_data = image_file.read() 

    #encodes the binary data using Base64 encoding
    base_64_encoded_data = base64.b64encode(binary_data) 

    #decodes base_64_encoded_data from bytes to a string
    base64_string = base_64_encoded_data.decode('utf-8')


messages = [
    {
        "role": "user",
        "content": [{
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": base64_string
            },
        }]
    }
]

response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2048,
    messages=messages
)
print(response.content[0].text)