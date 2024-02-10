from django.conf import settings
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_summary(text):
    if api_key is None:
        return "No API key found"
    else:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": f"Summarize this for a TLDR: {text}"}]
        )
        summary = response.choices[0].message.content
        return summary