from openai import OpenAI

client = OpenAI()

history = [
    {"role": "user", "content": "My name is karam and I study Computer Science in Hungary"},
]

response = client.responses.create(
    model="gpt-5.5",
    input=history
)

history.append({"role": "assistant", "content": response.output_text})
history.append({"role": "user", "content": "what do i study and where?"})

response2 = client.responses.create(
    model="gpt-5.5",
    input=history
)

print(response2.output_text)
