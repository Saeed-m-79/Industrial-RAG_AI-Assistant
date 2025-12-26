from groq import Groq


def query_groq(api_key: str, prompt: str):
    client = Groq(api_key=api_key)

    chat = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return chat.choices[0].message.content
