# ML Model REST API

This repository is a **Proof of Concept (PoC)** for serving **Machine Learning (ML) models** via a REST API using **FastAPI**, along with a simple interactive **Streamlit UI**. It supports the following pre-trained classification models:

- Text **Sentiment Classification**
- Text **Disaster Classification**
- Human **Pose Image Classification**

---
## Client & Server

If you encounter any issues with the API, please visit the [Hugging Face Space](https://huggingface.co/spaces/fahmiaziz/ml-model-restapi) and restart the application.

- **Streamlit UI**: [https://ml-model-serving-ui.streamlit.app/](https://ml-model-serving-ui.streamlit.app/)  
  Access the interactive user interface to test the models easily.

- **API Documentation**: [https://fahmiaziz-ml-model-restapi.hf.space/docs](https://fahmiaziz-ml-model-restapi.hf.space/docs)  
  Explore the API documentation and test endpoints directly via Swagger UI.
## Features

- **Sentiment Analysis**: Predicts if a given text expresses positive or negative sentiment.
- **Disaster Detection**: Determines whether the text is related to a disaster.
- **Pose Image Classification**: Classifies human poses from an input image.
- **Streamlit UI**: Interactive user interface to access the models easily.

---

## Project Structure

```
├── app.py                     # FastAPI main entry point
├── streamlit_app.py           # Streamlit-based UI interface
│
├── router/                    # FastAPI route handlers for each model
│   ├── disaster.py            # Disaster classification endpoint
│   ├── sentiment.py           # Sentiment classification endpoint
│   └── image_clf.py           # Pose classification endpoint
│
├── scripts/                   # Utility scripts
│   ├── data_model.py          # Pydantic request/response schemas
│   └── s3.py                  # S3 helper functions for upload/download
│
├── utils/                     # General utilities
│   ├── log.py                 # Logging configuration
│   └── pipeline.py            # Model loading and inference pipelines
│
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── .env.example               # Example environment variables
└── README.md                  # Project documentation
```

## API Endpoints

| Task                      | Endpoint URL                             | Method |
|---------------------------|------------------------------------------|--------|
| Sentiment Classification  | `POST /api/v1/sentiment_classification`  | JSON   |
| Disaster Classification   | `POST /api/v1/disaster_classification`   | JSON   |
| Pose Image Classification | `POST /api/v1/image_classification`      | JSON   |

**Sample Payload for Image Classification**:

```json
{
  "user_id": "123vb",
  "url": ["https://example.com/sample.jpg"]
}
```

## Deploy API via Hugging Face Spaces (Recommended)
For a step-by-step guide on [deploying applications on Hugging Face Spaces](https://huggingface.co/blog/HemanthSai7/deploy-applications-on-huggingface-spaces), please visit Deploy Applications on Hugging Face Spaces.
