import os
import time
from typing import Union
from fastapi import APIRouter
from scripts.data_model import ClassificationInput, ClassificationOutput
from utils.pipeline import load_model

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
MODEL_PATH = os.path.join(BASE_DIR, "ml-models", "tinybert-disaster-tweet/")

@router.post(
    "/disaster_classification",
    response_model=ClassificationOutput,
    summary="Disaster Classification",
    description="Classify the disaster of a given text using a pre-trained model."
)
def disaster_classification(input: ClassificationInput)-> ClassificationOutput:
    try:
        pipe = load_model(MODEL_PATH)
        start = time.time()
        output = pipe(input.text)
        end = time.time()
        prediction_time = int((end-start)*1000)

        labels = [x['label'] for x in output]
        scores = [x['score'] for x in output]

        return ClassificationOutput(
            user_id=input.user_id,
            text=input.text,
            model_name="tinybert-disaster-tweet",
            sentiment=labels,
            score=scores,
            prediction_time=prediction_time
        )
        
    except Exception as e:
        return {"error": f"Failed to process text classification: {str(e)}"}, 500