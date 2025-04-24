from dotenv import load_dotenv
from anthropic import Anthropic

#load environment variable
load_dotenv()

#automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()

## Important:
# rotating roles 

# response = client.messages.create(
#     model="claude-3-5-haiku-20241022",
#     max_tokens=100,
#     messages = [
#         {"role": "user", "content": "Hello Claude! How are you today?"},
#         {"role": "assistant", "content": "Hello! I'm doing well, thank you. How can I assist you today?"},
#         {"role": "user", "content": "Can you tell me a fun fact about ferrets?"},
#         {"role": "assistant", "content": "Sure! Did you know that excited ferrets make a clucking vocalization known as 'dooking'?"},
#     ]
# )

# response = client.messages.create(
#     model="claude-3-haiku-20240307",
#     max_tokens=1000,
#     messages=[
#         {"role": "user", "content": "Translate hello to French. Respond with a single word"}
#     ]
# )

# def translate(word, language):
#     response = client.messages.create(
#         model = "claude-3-5-haiku-20241022",
#         max_tokens= 100,
#         messages = [
#             {"role": "user", "content": f"Translate the word {word} into {language}. Only repsond with the translated workd, nothing else"}
#         ]
#     )
#     return response.content[0].text

# print(translate("hello", "Chinese"))
# print(translate("chicken", "Italian"))
# print(translate("ocean", "Spanish"))

# response = client.messages.create(
#     model="claude-3-haiku-20240307",
#     max_tokens=500,
#     messages=[
#         {"role": "user", "content": "Unpopular opinion: Pickles are disgusting. Don't @ me"},
#         {"role": "assistant", "content": "NEGATIVE"},
#         {"role": "user", "content": "I think my love for pickles might be getting out of hand. I just bought a pickle-shaped pool float"},
#         {"role": "assistant", "content": "POSITIVE"},
#         {"role": "user", "content": "Seriously why would anyone ever eat a pickle?  Those things are nasty!"},
#         {"role": "assistant", "content": "NEGATIVE"},
#         {"role": "user", "content": "Just tried the new spicy pickles from @PickleCo, and my taste buds are doing a happy dance! 🌶️🥒 #pickleslove #spicyfood"},
#     ]
# )
# print(response.content[0].text)

conversation_history = []

while True:
    user_input = input("User: ")

    if user_input.lower() == 'quit':
        print("Conversation ended.")
        break

    conversation_history.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model = 'claude-3-5-haiku-20241022',
        max_tokens = 500,
        messages=conversation_history
    )

    assistant_response = response.content[0].text
    print(f"Assistant: {assistant_response}")
    conversation_history.append({"role": "assistant", "content": assistant_response})