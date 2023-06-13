import openai
import chainlit as cl
from env_config import Config

openai.api_key = Config.OPENAI_API_KEY

model_name = "gpt-3.5-turbo"
settings = {
    "temperature": 0.7,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}


@cl.on_chat_start
def start_chat():
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "You are a helpful assistant."}],
    )


@cl.on_message
def main(message: str):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message})

    msg = cl.Message(content="")

    response = openai.ChatCompletion.create(
        model=model_name, messages=message_history, stream=True, **settings
    )
    for resp in response:
        token = resp.choices[0]["delta"].get("content", "")
        msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    msg.send()
