from openai import OpenAI
import json

client = OpenAI()


def get_weather(city):
    return f"It's 22°C and sunny in {city}"  # fake number as per now


tools = [{
    "type": "function",
    "name": "get_weather",
    "description": "Get current weather for a city",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "City name"}
        },
        "required": ["city"]
    }
}]

response = client.responses.create(
    model="gpt-5.5",
    input="write me a hiku",
    tools=tools
)

for item in response.output:
    if item.type == "function_call":
        args = json.loads(item.arguments)
        result = get_weather(args["city"])
        print("Model wants to call", item.name, args)
        print("Function result: ", result)
