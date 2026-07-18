from openai import OpenAI
import json

client = OpenAI()


def get_weather(city):
    return f"It's 22°C and sunny in {city}"


tools = [{
    "type": "function",
    "name": "get_weather",
    "description": "Get current weather for a city",
    "parameters": {
        "type": "object",
        "properties": {"city": {"type": "string"}},
        "required": ["city"]
    }
}]

history = []

print("Chat with your assistant. Type 'quit' to stop.")

while True:
    user_input = input("You: ")
    if user_input == "quit":
        break

    # TODO 1: append a user message to `history`
    # format: {"role": "user", "content": user_input}

    history.append({"role": "user", "content": user_input})

    response = client.responses.create(
        model="gpt-5.5",
        input=history,
        tools=tools
    )

    # TODO 2: loop through response.output
    # - if item.type == "function_call": parse args, call get_weather(),
    #   then append BOTH the function call and its result back into history
    #   (hint: you need item.call_id, item.name, item.arguments,
    #    and a {"type": "function_call_output", "call_id": ..., "output": ...} entry)
    # - if item.type == "message": print the assistant's reply and
    #   append {"role": "assistant", "content": response.output_text} to history

    for item in response.output:
        if item.type == "function_call":
            args = json.loads(item.arguments)
            result = get_weather(args["city"])
            print("Model wants to call", item.name, args)
            print("Function result: ", result)

            history.append(item)
            history.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": result
            })

            response = client.responses.create(
                model="gpt-5.5",
                input=history,
                tools=tools
            )
            print(response.output_text)

            history.append({
                "role": "assistant",
                "content": response.output_text
            })

        elif item.type == "message":
            print(response.output_text)
            history.append(
                {"role": "assistant", "content": response.output_text})
