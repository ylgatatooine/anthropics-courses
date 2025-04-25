from anthropic import Anthropic
from dotenv import load_dotenv

import base64

load_dotenv()
client = Anthropic()

# messages = [
#     {"role": "user", "content": "tell me a joke"}
# ]

# messages = [
#     {
#         "role": "user",
#         "content": [
#             {"type": "text", "text": "tell me a joke"},
#         ]
#     }
# ]

# messages = [
#     {
#         "role": "user",
#         "content": [
#             {"type": "text", "text": "who"},
#             {"type": "text", "text": "made"},
#             {"type": "text", "text": "you?"},
#         ]
#     }
# ]


## images and texts 
## ------------

# with open("./images/uh_oh.png", "rb") as image_file:
#     # binary_data = image_file.read()
#     # base_64_encoded_data = base64.b64encode(binary_data)
#     # base64_string = base_64_encoded_data.decode('utf-8')

#     #reads the contents of the image as a bytes object
#     binary_data = image_file.read() 

#     #encodes the binary data using Base64 encoding
#     base_64_encoded_data = base64.b64encode(binary_data) 

#     #decodes base_64_encoded_data from bytes to a string
#     base64_string = base_64_encoded_data.decode('utf-8')



# messages = [
#     {
#         "role": "user",
#         "content": [{
#             "type": "image",
#             "source": {
#                 "type": "base64",
#                 "media_type": "image/png",
#                 "data": base64_string
#             },
#         },
#         {
#             "type": "text",
#             "text": "What could this person have done to prevent this?"
#         }]
#     }
# ]

# response = client.messages.create(
#     model="claude-3-5-sonnet-20240620",
#     max_tokens=2048,
#     messages=messages
# )
# print(response.content[0].text)


## multiple images 
# messages = [
#     {
#         "role": "user",
#         "content": [
#             {
#                 "type": "image",
#                 "source": {
#                     "type": "base64",
#                     "media_type": image1_media_type,
#                     "data": image1_data,
#                 },
#             },
#             {
#                 "type": "image",
#                 "source": {
#                     "type": "base64",
#                     "media_type": image2_media_type,
#                     "data": image2_data,
#                 },
#             },
#             {
#                 "type": "image",
#                 "source": {
#                     "type": "base64",
#                     "media_type": image3_media_type,
#                     "data": image3_data,
#                 },
#             },
#             {"type": "text", "text": "How are these images different?"},
#         ],
#     }
# ]


import base64
import mimetypes

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

messages = [
    {
        "role": "user",
        "content": [
            create_image_message("./images/animal1.png")
        ]
    }
]

response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2048,
    messages=messages
)
print(response.content[0].text)