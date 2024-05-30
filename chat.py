from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


def chat_with_model(prompt):
    completion = client.chat.completions.create(
        model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )

    return completion.choices[0].message.content.strip()
