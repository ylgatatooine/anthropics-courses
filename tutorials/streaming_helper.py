from anthropic import AsyncAnthropic
import asyncio

client = AsyncAnthropic()

# client.messages.stream which gives us access to useful helper methods. client.messages.stream() returns a MessageStreamManager, which is a context manager that yields a MessageStream which is iterable, emits events, and accumulates messages.
# The code below uses client.messages.stream which allows us to use helpers like stream.text_stream to easily access generated text content as it streams in, without having to manually check the stream event type. stream.text_stream provides an iterator over just the text deltas in the stream.

async def streaming_with_helpers():
    async with client.messages.stream(
        model="claude-3-opus-20240229",
        max_tokens=512,
        messages=[
            {
                "role": "user",
                "content": "Write me sonnet about orchids",
            }
        ],
    ) as stream:
        async for text in stream.text_stream:
            print(text, end="", flush=True)

    final_message = await stream.get_final_message()
    print("\n\nSTREAMING IS DONE. HERE IS THE FINAL ACCUMUATED MESSAGE: ")
    print(final_message.to_json())

if __name__ == "__main__":
    asyncio.run(streaming_with_helpers())