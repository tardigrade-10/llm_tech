'''
Before running this script, create a .env file containing: OPENAI_API_KEY=<your api key>
create a venv with python>=3.10 and install poetry with `pip install poetry`
then run `poetry lock` to sync the dependencies and then run `poetry install`
after than simply run this script with `python openagent_check.py`
'''

import re
from openagent import compiler
from openagent.llms._openai import OpenAI

# load .env file in format:
# OPENAI_API_KEY=sk-xxx
from dotenv import load_dotenv
load_dotenv()


llmcc = OpenAI(
    model="gpt-3.5-turbo"
)

llmtc = OpenAI(
    model="text-davinci-003"
)

# test case to check chat loop: works

chat_loop = compiler(
                '''{{#system}}You are a helpful assistant{{/system}}

                    {{~#genach 'conversation' stop=False}}

                    {{#user~}}
                    {{set 'this.user_text' (await 'user_text') hidden=False}}
                    {{~/user}}

                    {{#assistant~}}
                    {{gen 'this.response' temperature=0 max_tokens=300}}
                    {{~/assistant}}
                    
                    {{~/geneach}}''', llm = llmcc) 


# manual conversation (in manual conversation, next input must be provide to return value)
# chat_loop2 = chat_loop1(user_text = "My name is yash") # chat_loop2 has the conversation of chat_loop1
# chat_loop3 = chat_loop2(user_text = "What is my name?") # chat_loop3 has the conversation of chat_loop2


# chat loop (in a loop, both function (chat_loop1) and returned value (chat_loop2) should have same name)
n = 0
while n < 5:
    chat_loop = chat_loop(user_text = input())
    print("AI:", chat_loop['conversation'][-2]['response'] + '\n')
    n += 1
