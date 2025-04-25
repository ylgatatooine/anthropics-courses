from anthropic import AsyncAnthropic, AsyncMessageStream
import asyncio

client = AsyncAnthropic()

green = '\033[32m'
reset = '\033[0m'

class MyStream(AsyncMessageStream):
    async def on_text(self, text, snapshot):
        # This runs only on text delta stream messages
        print(green + text + reset, flush=True) #model generated content is printed in green

    async def on_stream_event(self, event):
        # This runs on any stream event
        print("on_event fired:", event.type)

async def streaming_events_demo():
    async with client.messages.stream(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Generate a 5-word poem",
            }
        ],
        model="claude-3-opus-20240229",
        event_handler=MyStream, 
    ) as stream:
        # Get the final accumulated message, after the stream is exhausted
        message = await stream.get_final_message()
        print("accumulated final message: ", message.to_json())

if __name__ == "__main__":
    asyncio.run(streaming_events_demo())