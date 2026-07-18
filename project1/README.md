# AI Weather Assistant with Function Calling

A Python chatbot that uses the OpenAI Responses API and function calling to answer weather-related questions.

## About

This project demonstrates how an LLM can interact with external Python functions using OpenAI's function calling feature.

Instead of making up weather information, the model determines when it needs weather data, requests the appropriate function, receives the result, and uses it to generate a natural-language response.

For learning purposes, the weather function currently returns simulated weather data.

## Features

- Interactive command-line chatbot
- Conversation history
- OpenAI Function Calling
- Automatic weather function invocation
- Multi-turn conversations
- JSON argument parsing

## Technologies Used

- Python
- OpenAI Python SDK
- JSON

## How It Works

1. The user sends a message.
2. The message is stored in the conversation history.
3. The OpenAI model analyzes the request.
4. If weather information is needed, the model requests the `get_weather()` function.
5. Python executes the function.
6. The function result is sent back to the model.
7. The model generates a natural-language response using the returned data.

## Example

### User

```text
What's the weather like in Pécs?
```

### Function Call

```text
get_weather(city="Pécs")
```

### Function Result

```text
It's 22°C and sunny in Pécs.
```

### Assistant

```text
The weather in Pécs is currently 22°C and sunny.
```

## Concepts Learned

- OpenAI Responses API
- Function Calling
- Tool Definitions
- JSON Schemas
- Conversation History
- Multi-turn Conversations
- Python Functions
- Parsing Function Arguments

## Future Improvements

- Connect to a real weather API (OpenWeatherMap or Open-Meteo)
- Support multiple tools (weather, news, time, etc.)
- Handle multiple function calls in a single conversation
- Add streaming responses
- Build a graphical user interface
- Deploy as a web application

## Project Structure

```
weather-assistant/
│
├── weather_assistant.py
├── README.md
└── .gitignore
```

## Author

Karam Alnajjar