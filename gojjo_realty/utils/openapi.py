from openai import OpenAI
from config.settings.base import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_summary(text):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": f"Summarize this for a TLDR: {text}"}]
        )
        summary = response.choices[0].message.content
        return summary