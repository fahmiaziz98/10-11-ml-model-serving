import os
import time
from fastapi import APIRouter, HTTPException
from scripts.data_model import ImageInput, ImageOutput
from utils.pipeline import load_model
from utils.log import logger

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
MODEL_PATH = os.path.join(BASE_DIR, "ml-models", "vit-human-pose-classification/")

@router.post(
    "/image_classification",
    response_model=ImageOutput,
    summary="Image Classification",
    description="Classify the image using a pre-trained model."
)
def image_classification(input: ImageInput)-> ImageOutput:
    """
    Classify the image using a pre-trained model.
    
    Args:
        input (ImageInput): The input data containing the image URL and user ID.
    
    Returns:
        ImageOutput: The output data containing the labels, scores, prediction time, and other info.
    """
    try:
        pipe = load_model(MODEL_PATH, is_image_model=True)
        image = input.url
        logger.info(f"Image URLs: {image[-1]}")
        
        start = time.time()
        output = pipe(image[-1])
        end = time.time()
        prediction_time = int((end - start) * 1000) 
        
        labels = [x["label"] for x in output]
        scores = [x["score"] for x in output]

        return ImageOutput(
            user_id=input.user_id,
            url=input.url,
            model_name="vit-human-pose-classification",
            label=labels,
            score=scores,
            prediction_time=prediction_time
        )
   
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process image classification: {e}")