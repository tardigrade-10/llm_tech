from langflow import load_flow_from_json

flow = load_flow_from_json("Calculator.json")
# Now you can use it like any chain
flow("Hey, have you heard of LangFlow?")