from fastapi import FastAPI, UploadFile, File
from agent import ask_farmer_ai, generate_farming_checklist
from image_agent import analyze_crop_image
import shutil
import os
from weather import get_weather
from memory import get_memory
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Farmer AI Assistant")

@app.get("/")
def home():
    return {"message": "Farmer AI is running"}

# 🧠 Ask question
@app.post("/ask")
# async def ask(question: str):
#     answer = ask_farmer_ai(question)
#     return {"response": answer}
async def ask(question: str):
    answer = ask_farmer_ai(question, user_id="farmer1")
    return {"response": answer}

# 🖼️ Upload image
@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_crop_image(file_path)
    return {"analysis": result}

# Farmer checklist

@app.post("/farming-checklist")
async def farming_checklist(crop: str):
    result = generate_farming_checklist(crop)
    return {"result": result}

@app.get("/memory")
def view_memory():
    return get_memory("farmer1")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# @app.post("/farming-checklist")
# async def farming_checklist(crop: str):
#     answer = farming_checklist(crop = 'Paddy')
#     return {"result": answer }
# def farming_checklist(crop: str):
#     weather = get_weather()

#     prompt = f"""
# Create a simple farming checklist for growing {crop} in India.

# Current Weather:
# Temperature: {weather['temp']}°C
# Condition: {weather['condition']}
# Humidity: {weather['humidity']}%

# Give:
# 1. Land preparation
# 2. Seed selection
# 3. Watering plan
# 4. Fertilizer plan
# 5. Pest control
# 6. Weather precautions
# 7. Low-cost tips

# Keep it simple for farmers.
# """

#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     return {"result": response.choices[0].message.content}