from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scripts.s3 import download_model_from_s3
from router.disaster import router as disaster_router
from router.sentiment import router as sentiment_router
from router.image_clf import router as image_router
from utils.log import logger


app = FastAPI(
    title="ML API",
    description="ML API for sentiment analysis and image classification",
    version="0.0.1",
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

 
sentiment_model_path = "ml-models/tinybert-sentiment-analysis/"
disaster_model_path = "ml-models/tinybert-disaster-tweet/"
image_model_path = "ml-models/vit-human-pose-classification/"

logger.info("Ensuring models are downloaded...")
download_model_from_s3(sentiment_model_path, sentiment_model_path)
download_model_from_s3(disaster_model_path, disaster_model_path)
download_model_from_s3(image_model_path, image_model_path)
logger.info("All models are ready.")


@app.get("/")
def read_root():
    return {"Status": "Running"}
  

app.include_router(disaster_router, prefix="/api/v1", tags=["Disaster"])
app.include_router(sentiment_router, prefix="/api/v1", tags=["Sentiment"])
app.include_router(image_router, prefix="/api/v1", tags=["Image"])