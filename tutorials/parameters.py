## max_token: 1 token is about 3.5 English characters

## Response' stop_reason shows why the response stopped. 
### end_turn is the way of naturally finished generating. 
### max_token is the way of saying the end reached. 

from dotenv import load_dotenv
from anthropic import Anthropic

#load environment variable
load_dotenv()

#automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()

# truncated_response = client.messages.create(
#     model="claude-3-haiku-20240307",
#     max_tokens=10,
#     messages=[
#         {"role": "user", "content": "Write me a poem"}
#     ]
# )
# print(truncated_response.content[0].text)

# print(truncated_response.usage.output_tokens)
# print(truncated_response.stop_reason)

# import time
# def compare_num_tokens_speed():
#     token_counts = [50,500,2000]
#     task = """
#         Create a long, detailed dialogue that is at least 5000 words long between two characters discussing the impact of social media on mental health. 
#         The characters should have differing opinions and engage in a respectful thorough debate.
#     """

#     for num_tokens in token_counts:
#         start_time = time.time()

#         response = client.messages.create(
#             model="claude-3-haiku-20240307",
#             max_tokens=num_tokens,
#             messages=[{"role": "user", "content": task}]
#         )

#         end_time = time.time()
#         execution_time = end_time - start_time

#         print(f"Number of tokens generated: {response.usage.output_tokens}")
#         print(f"Execution Time: {execution_time:.2f} seconds\n")


# compare_num_tokens_speed()

# (.venv) (base) lianggangyu@MacBookPro tutorials % python parameters.py
# Number of tokens generated: 50
# Execution Time: 0.81 seconds

# Number of tokens generated: 500
# Execution Time: 3.47 seconds

# Number of tokens generated: 2000
# Execution Time: 15.27 seconds


# response = client.messages.create(
#     model="claude-3-haiku-20240307",
#     max_tokens=100,
#     messages=[{"role": "user", "content": "Generate a JSON object representing a person with a name, email, and phone number ."}],
#     stop_sequences=["}"]
# )
# print(response.content[0].text)
# print(response.stop_reason)

# (.venv) (base) lianggangyu@MacBookPro tutorials % python parameters.py
# Here's a JSON object representing a person with a name, email, and phone number:

# {
#   "name": "John Doe",
#   "email": "johndoe@example.com",
#   "phone": "555-1234"

# stop_sequence


# def generate_random_letters_3_times():
#     for i in range(3):
#         response = client.messages.create(
#             model="claude-3-haiku-20240307",
#             max_tokens=500,
#             messages=[{"role": "user", "content": "generate a poem"}],
#             stop_sequences=["b", "c"]
#         )
#         print(f"Response {i+1} stopped because {response.stop_reason}.  The stop sequence was {response.stop_sequence}")
#         print(response.content[0].text)

# generate_random_letters_3_times()


# use temperature 0 for analytics tasks, 1 for creative and generative tasks
# Anthropic Claude default temperature is 1.

# def demonstrate_temperature():
#     temperatures = [0, 1]
#     for temperature in temperatures:
#         print(f"Prompting Claude three times with temperature of {temperature}")
#         print("================")
#         for i in range(3):
#             response = client.messages.create(
#                 model="claude-3-haiku-20240307",
#                 max_tokens=50,
#                 messages=[{"role": "user", "content": "Come up with a name for an alien planet. Respond with a single word."}],
#                 temperature=temperature
#             )
#             print(f"Response {i+1}: {response.content[0].text}")

# demonstrate_temperature()

# (.venv) (base) lianggangyu@MacBookPro tutorials % python parameters.py
# Prompting Claude three times with temperature of 0
# ================
# Response 1: Xendor.
# Response 2: Xendor.
# Response 3: Xendor.
# Prompting Claude three times with temperature of 1
# ================
# Response 1: Xenosis.
# Response 2: Xenos.
# Response 3: Zyloth.


# system prompt give Claude high level instructions, defining its role, and provide background info about its responses. 
#         
message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    system="You are a helpful foreign language tutor that always responds in French.",
    messages=[
        {"role": "user", "content": "Hey there, how are you?!"}
    ]
)

print(message.content[0].text)