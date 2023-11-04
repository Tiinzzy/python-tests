from typing import Optional
from pydantic import BaseModel, confloat
from fastapi import FastAPI
import joblib

# some documentation in markdown
description = "Hi there"

app = FastAPI(
    title="Tina Personal Company",
    version="0.1",
    description="I started this company in 2022 when I formally moved to Montreal to "
                "open new horizons in my professional life!"

)

model = joblib.load("./resources/model.joblib")


class Features(BaseModel):
    sepal_length: confloat(ge=0.0, le=1.0)
    sepal_width: confloat(ge=0.0, le=1.0)
    petal_length: confloat(ge=0.0, le=1.0)
    petal_width: confloat(ge=0.0, le=1.0)

    class Config:
        schema_extra = {
            "example": {
                "sepal_length": 0.2,
                "sepal_width": 0.5,
                "petal_length": 0.8,
                "petal_width": 1.0,
            }
        }


class Response(BaseModel):
    setosa_probability: confloat(ge=0.0, le=1.0)
    versicolor_probability: confloat(ge=0.0, le=1.0)
    virginica_probability: confloat(ge=0.0, le=1.0)

    class Config:
        schema_extra = {
            "example": {
                "setosa_probability": 0.7,
                "versicolor_probability": 0.1,
                "virginica_probability": 0.2,
            }
        }


@app.post("/predict/", response_model=Response)
def predict(features: Features):
    feature_list = [
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.sepal_width,
    ]
    predictions = model.predict_proba([feature_list])[-1]
    predictions_clean = Response(
        setosa_probability=predictions[0],
        versicolor_probability=predictions[1],
        virginica_probability=predictions[2],
    )
    return predictions_clean
