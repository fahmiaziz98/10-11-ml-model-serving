from pydantic import BaseModel
from typing import List


class ClassificationInput(BaseModel):
    user_id: str
    text: List[str]

class ImageInput(BaseModel):
    user_id: str
    url: List[str]


class ClassificationOutput(BaseModel):
    user_id: str
    text: List[str]
    model_name: str
    sentiment: List[str]
    score: List[float]
    prediction_time: int

class ImageOutput(BaseModel):
    user_id: str
    url: List[str]
    model_name: str
    label: List[str]
    score: List[float]
    prediction_time: int