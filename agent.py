from groq import Groq
import os
from weather import get_weather
from memory import save_memory, get_memory

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_farmer_ai(question: str, user_id: str = "farmer1"):
    weather = get_weather()
    previous = get_memory(user_id)

    previous_context = ""
    if previous:
        previous_context = f"""
Previous Interaction:
{previous}
"""

    weather_info = ""
    if weather:
        weather_info = f"""
Current Weather:
city:{weather['city']}
Temperature: {weather['temp']}°C
Condition: {weather['condition']}
Humidity: {weather['humidity']}%
"""

    prompt = f"""
You are an agriculture expert helping farmers in India.

{previous_context}
{weather_info}

Answer the question clearly and simply.

Also refer to previous context if relevant.

Question: {question}

Give:
1. Problem explanation
2. Cause
3. Step-by-step solution
4. Weather-based advice (VERY IMPORTANT)
5. Low-cost tips
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content

    # ✅ Save memory
    save_memory(user_id, "last_question", question)
    save_memory(user_id, "last_answer", answer)

    return answer

def generate_farming_checklist(crop: str):
    weather = get_weather()

    weather_info = ""
    if weather:
        weather_info = f"""
Current Weather:
Temperature: {weather['temp']}°C
Condition: {weather['condition']}
Humidity: {weather['humidity']}%
"""

    prompt = f"""
You are an agriculture expert helping farmers in India.

Create a simple farming checklist for growing {crop}.

{weather_info}

Give:
1. Land preparation
2. Seed selection
3. Watering plan
4. Fertilizer plan
5. Pest control
6. Weather precautions
7. Low-cost tips

Keep it simple and practical.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def generate_farming_checklist(crop: str):
    weather = get_weather()

    weather_info = ""
    if weather:
        weather_info = f"""
Current Weather:
Temperature: {weather['temp']}°C
Condition: {weather['condition']}
Humidity: {weather['humidity']}%
"""

    prompt = f"""
You are an agriculture expert helping farmers in India.

Create a simple farming checklist for growing {crop}.

{weather_info}

Give:
1. Land preparation
2. Seed selection
3. Watering plan
4. Fertilizer plan
5. Pest control
6. Weather precautions
7. Low-cost tips

Keep it simple and practical.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content