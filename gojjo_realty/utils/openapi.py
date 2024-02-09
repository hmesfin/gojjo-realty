# from django.conf import settings
# from openai import OpenAI


# api_key = settings.OPENAI_API_KEY

# client = OpenAI(api_key=api_key)

# def generate_summary(text):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "system", "content": "You are a helpful assistant."},
#                   {"role": "user", "content": f"Summarize this for a TLDR: {text}"}]
#     )
#     summary = response.choices[0].message.content
#     return summary