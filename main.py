import pandas as pd
import joblib
from fastapi import FastAPI, Request
from pydantic import BaseModel
import numpy as np


model = joblib.load('final_model.pkl')

app = FastAPI()

class InputData(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str
@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/predict")
def predict_insurance(data: InputData):
    data_dict = data.model_dump()
    df = pd.DataFrame([data_dict])
    prediction = model.predict(df)
    return {"prediction": float(prediction[0])}
    