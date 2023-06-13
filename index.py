import os
import openai
from env_config import Config

openai.api_key = Config.OPENAI_API_KEY

message = ["hi", "i have a cat", "can you suggest a name for her"]
for i in range(3):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": """Please provide a detailed guide on how to effectively house train a dog. Your response should include step-by-step instructions, helpful tips, and potential challenges that may arise during the process. Please also consider addressing common mistakes or misconceptions about house training and offering practical solutions to overcome them. Your guide should be easy to follow and catered to different types of dogs and their individual needs. Lastly, your response should emphasize positive reinforcement and patience as key components in successfully house training a dog."""}
    ],
    n = 1
    )
    print(completion)

