import os
from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl

from env_config import Config

os.environ["OPENAI_API_KEY"] = Config.OPENAI_API_KEY

template = """Question: {question}

Answer: Let's think step by step."""

@cl.langchain_factory
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0), verbose=True)

    return llm_chain
