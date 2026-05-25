from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="KrishiPrajna API",
    description="AI Powered Smart Agriculture Platform",
    version="1.0.0"
)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "KrishiPrajna Backend Running Successfully"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "KrishiPrajna Backend"
    }

@app.get("/sensor-data")
def get_sensor_data():
    return {
        "temperature": 30,
        "humidity": 65,
        "soil_moisture": 42,
        "rain_detected": False,
        "motor_status": "OFF"
    }

@app.get("/weather")
def weather_data():
    return {
        "location": "Andhra Pradesh",
        "temperature": 31,
        "humidity": 60,
        "condition": "Cloudy",
        "rain_probability": 45
    }

@app.get("/irrigation-prediction")
def irrigation_prediction():
    return {
        "crop": "Rice",
        "soil_moisture": 42,
        "recommended_irrigation": True,
        "recommended_duration_minutes": 20
    }
