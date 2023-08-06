import guidance
import re
from env_config import Config
guidance.llm = guidance.llms.OpenAI("gpt-3.5-turbo", api_key = Config.OPENAI_API_KEY)


role_simulator = guidance('''
{{#system~}}
You are a helpful assistant
{{~/system}}

{{#user~}}
You will answer the user as {{role}} in the following conversation. At every step, I will provide you with the user input, as well as a comment reminding you of your instructions. Never talk about the fact that you are an AI, even if the user asks you. Always answer as {{role}}.
{{#if first_question}}You can also start the conversation.{{/if}}
{{~/user}}

{{~! The assistant either starts the conversation or not, depending on if this is the first or second agent }}
{{#assistant~}}
Ok, I will follow these instructions.
{{#if first_question}}Let me start the conversation now:
{{role}}: {{first_question}}{{/if}}
{{~/assistant}}

{{~! Then the conversation unrolls }}
{{~#geneach 'conversation' stop=False}}
{{#user~}}
User: {{set 'this.input' (await 'input')}}
Comment: Remember, answer as a {{role}}. Start your utterance with {{role}}:
{{~/user}}

{{#assistant~}}
{{gen 'this.response' temperature=0 max_tokens=300}}
{{~/assistant}}
{{~/geneach}}''')

republican = role_simulator(role='Republican', await_missing=True)
democrat = role_simulator(role='Democrat', await_missing=True)

first_question = '''What do you think is the best way to stop inflation?'''
republican = republican(input=first_question, first_question=None)
democrat = democrat(input=republican["conversation"][-2]["response"].strip('Republican: '), first_question=first_question)
for i in range(2):
    republican = republican(input=democrat["conversation"][-2]["response"].replace('Democrat: ', ''))
    democrat = democrat(input=republican["conversation"][-2]["response"].replace('Republican: ', ''))

print('Democrat: ' + first_question)
for x in democrat['conversation'][:-1]:
    print('Republican:', x['input'])
    print()
    print(x['response'])
