# from google import 
# import os

# client = genai.Client(
#     api_key=os.getenv("GOOGLE_API_KEY"),
# )

# for model in client.models.list():
#     print(model.name)

# response = client.models.generate_content(
#     model="gemini-1.5-flash",   # keep simple name (NOT models/...)
#     contents="Say hello like a farmer assistant"
# )

# print(response.text)

# import google.generativeai as genai
# import os

# key = os.environ.get('GOOGLE_API_KEY')
# print(f"[{key}]")

# genai.configure(api_key=os.environ[ 'GOOGLE_API_KEY' ])

# model = genai.GenerativeModel(model_name='gemini-1.5-flash-8b')
# response = model.generate_content('Teach me about how an LLM works')

#### print(response.text)

import os
from groq import Groq

# 1. Initialize the Groq client
# It will automatically look for the "GROQ_API_KEY" environment variable
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# 2. Create the request
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful Farmer Assistant. Provide practical, easy-to-understand agricultural advice."
        },
        {
            "role": "user",
            "content": "How does an LLM work? Explain it using a farming analogy.",
        }
    ],
    # This is a powerful, smart model available on the free tier
    model="llama-3.3-70b-versatile",
)

# 3. Print the response
print(chat_completion.choices[0].message.content)