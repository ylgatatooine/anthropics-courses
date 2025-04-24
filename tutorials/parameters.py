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

import time
def compare_num_tokens_speed():
    token_counts = [50,500,2000]
    task = """
        Create a long, detailed dialogue that is at least 5000 words long between two characters discussing the impact of social media on mental health. 
        The characters should have differing opinions and engage in a respectful thorough debate.
    """

    for num_tokens in token_counts:
        start_time = time.time()

        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=num_tokens,
            messages=[{"role": "user", "content": task}]
        )

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Number of tokens generated: {response.usage.output_tokens}")
        print(f"Execution Time: {execution_time:.2f} seconds\n")


compare_num_tokens_speed()

# (.venv) (base) lianggangyu@MacBookPro tutorials % python parameters.py
# Number of tokens generated: 50
# Execution Time: 0.81 seconds

# Number of tokens generated: 500
# Execution Time: 3.47 seconds

# Number of tokens generated: 2000
# Execution Time: 15.27 seconds