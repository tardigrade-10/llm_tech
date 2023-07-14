import guidance
from env_config import Config

# set the default language model used to execute guidance programs
guidance.llm = guidance.llms.OpenAI("gpt-3.5-turbo", api_key=Config.OPENAI_API_KEY)

valid_dish = ["Pizza", "Noodles", "Pho"]

# define the prompt
order_maker = guidance("""The following is a order in JSON format.
```json
{
    "name": "{{name}}",
    "age": {{gen 'age' pattern='[0-9]+' stop=','}},
    "delivery": "{{#select 'delivery'}}Yes{{or}}No{{/select}}",
    "order": "{{select 'order' options=valid_dish}}",
    "amount": {{gen 'amount' pattern='[0-9]+' stop=','}}
}```""")

# generate a character
order_maker(
    name="Alex",
    valid_dish=valid_dish
)