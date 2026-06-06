from anthropic.types import MessageParam
from agents.lm_studio_local import create_local_chat_model

model = "qwen/qwen3.5-9b"

client = create_local_chat_model()

messages: list[MessageParam] = []


def add_user_message(messages: list[MessageParam], text):
    messages.append({
        "role": "user",
        "content": text,
    })


def add_assistant_message(messages: list[MessageParam], text):
    messages.append({
        "role": "assistant",
        "content": text,
    })


def chat_message(
        messages: list[MessageParam],
        system_prompt: str | None = None,
        temperature: float | None = None,
        stop_sequences: list[str] | None = None,
):
    chat_response = chat_object(
        messages=messages,
        system_prompt=system_prompt,
        temperature=temperature,
        stop_sequences=stop_sequences,
    )
    return chat_response.content[0].text


def chat_object(
        messages: list[MessageParam],
        system_prompt: str | None = None,
        temperature: float| None = None,
        stop_sequences: list[str] | None = None,
):
    params: dict[str, str | int | float | list[MessageParam|str]] = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }

    if system_prompt is not None:
        params["system"] = system_prompt

    if temperature is not None:
        params["temperature"] = temperature

    if stop_sequences is not None:
        params["stop_sequences"] = stop_sequences

    return client.messages.create(**params)


