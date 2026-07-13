# OpenAI Function Calling Weather Tool

A beginner project exploring OpenAI's Responses API and function calling.

## What it does

- Sends a user request to GPT-5.5
- Allows the model to call a custom Python function
- Executes the function locally
- Returns the function result

## Concepts learned

- OpenAI Python SDK
- Responses API
- Tool calling
- JSON schemas
- Connecting LLMs with external functions

## Example

User:
"What is the weather like in Pécs?"

Model:
Requests the `get_weather` function.

Python:
Runs the function and returns the weather data.