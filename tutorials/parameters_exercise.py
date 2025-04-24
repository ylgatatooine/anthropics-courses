from dotenv import load_dotenv
from anthropic import Anthropic

#load environment variable
load_dotenv()

#automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()

def generate_questions(topic, number_questions):
    response = client.messages.create(
        model='claude-3-5-haiku-20241022',
        max_tokens=500,
        system=f"You are an expert on {topic}. Generate thought-provoking questions about this topic.",
        messages=[{
            "role": "user",
            "content": f"Generate {number_questions} questions about {topic} as a numbered list." 
        }],
        stop_sequences=[f"{number_questions + 1 }."]
    )

    print(response.content[0].text)
    print(response.stop_reason)
    print(response.stop_sequence)

generate_questions(topic="free will", number_questions=3)

