from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import numpy as np
from mlProject.pipeline.prediction import PredictionPipeline
import uvicorn
import os

app = FastAPI()

# setup templates
templates = Jinja2Templates(directory="templates")

# Home page → show form
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Train model
@app.get("/train")
def train():
    os.system("python main.py")
    return {"message": "Training Successful!"}

# HTML Form submission → predict salary
@app.post("/predict_form", response_class=HTMLResponse)
def predict_form(request: Request, years_experience: float = Form(...)):
    data = np.array([[years_experience]])
    obj = PredictionPipeline()
    prediction = obj.predict(data)
    return templates.TemplateResponse(
        "prediction.html",
        {"request": request, "prediction": float(prediction)}
    )
