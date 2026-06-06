import json

from chat_utils import *

# model = "claude-sonnet-4-0"
model = "qwen/qwen3.5-9b"

client = create_local_chat_model()

messages: list[MessageParam] = []



add_user_message(messages, "What is quantum computing? Answer in one sentence")

response = chat_message(messages)
print("\nanswer:\n", response.content[0].text)
add_assistant_message(messages, response.content[0].text)

add_user_message(messages, "Write another sentence")
response = chat_message(messages)
print("\nanswer:\n", response.content[0].text)

print("\nfull_response:\n", json.dumps(response.model_dump(), indent=2))

