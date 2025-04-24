from dotenv import load_dotenv
import os

load_dotenv()
my_api_key = os.getenv("ANTHROPIC_API_KEY")

print(my_api_key)
