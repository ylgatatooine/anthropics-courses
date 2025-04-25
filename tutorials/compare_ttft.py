from dotenv import load_dotenv
from anthropic import Anthropic
import time

load_dotenv()
client = Anthropic()

def compare_ttft():
    def measure_streaming_ttft():
        start_time = time.time()

        stream = client.messages.create(
            max_tokens=400,
            messages=[{
                "role": "user",
                "content": "Write me a very long essay explaining the history of Chinese Culture Revolution!",
            }],
            temperature = 0, 
            model="claude-3-opus-20240229",
            stream = True,
        )

        have_received_first_token = False
        for event in stream:
            if event.type == "content_block_delta":
                if not have_received_first_token:
                    ttft = time.time() - start_time
                    have_received_first_token = True
            elif event.type == "message_delta":
                output_tokens = event.usage.output_tokens
                total_time = time.time() - start_time
        return (ttft, output_tokens)
    
    def measure_non_streaming_ttft():
        start_time = time.time()

        response = client.messages.create(
            max_tokens=400,
            messages=[{
                "role": "user",
                "content": "Write me a very long essay explaining the history of Chinese Culture Revolution!",
            }],
            temperature = 0, 
            model="claude-3-opus-20240229",
        )
        ttft = time.time() - start_time
        return (ttft, response.usage.output_tokens)
    
    streaming_ttft, streaming_tokens = measure_streaming_ttft()
    non_streaming_ttft, non_streaming_tokens = measure_non_streaming_ttft()

    print("OPUS STREAMING")
    print(f"Time to first token: {streaming_ttft}")
    print(f"Tokens generated: {streaming_tokens}")
    print("#########################################################")
    print("OPUS NON STREAMING")
    print(f"Time to first token: {non_streaming_ttft}")
    print(f"Tokens generated: {non_streaming_tokens}")

compare_ttft()