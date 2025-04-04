import os
import time
from typing import Union
from fastapi import APIRouter
from scripts.data_model import ClassificationInput, ClassificationOutput
from utils.pipeline import load_model

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
MODEL_PATH = os.path.join(BASE_DIR, "ml-models", "tinybert-sentiment-analysis/")

@router.post(
    "/sentiment_classification",
    response_model=ClassificationOutput,
    summary="Sentiment Classification",
    description="Classify the sentiment of a given text using a pre-trained model."
)
def sentiment_classification(input: ClassificationInput)-> ClassificationOutput:
    """
    Classify the sentiment of a given text using a pre-trained model.

    Args:
        input (ClassificationInput): The input data containing the user_id and text.

    Returns:
        ClassificationOutput: The output data containing the user_id, text, model_name, sentiment, score, and prediction_time.

    """
    try:
        pipe = load_model(MODEL_PATH)
        start = time.time()
        output = pipe(input.text)
        end = time.time()
        prediction_time = int(( end - start) * 1000)

        labels = [x['label'] for x in output]
        scores = [x['score'] for x in output]

        return ClassificationOutput(
            user_id=input.user_id,
            text=input.text,
            model_name="tinybert-sentiment-analysis",
            sentiment=labels,
            score=scores,
            prediction_time=prediction_time
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process text classification: {e}")