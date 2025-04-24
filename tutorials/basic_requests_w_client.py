
from anthropic import Anthropic

client = Anthropic()  # anthropic SDK automatically ooks for an environment variable called "ANTHROPIC_API_KEY"

my_first_message = client.messages.create(
    model="claude-3-5-haiku-20241022",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Hi there, please tell me a joke about a pet robot dog"}
    ]
)

print(my_first_message.content[0].text)