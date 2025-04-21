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

## Setup and Installation

### Prerequisites
- Python 3.11 or later
- pip (Python package manager)
- Docker (optional, for containerized deployment)

### Installation Steps

1. **Install UV**
   ```bash
   curl -Ls https://astral.sh/uv/install.sh | bash
   export PATH="$HOME/.local/bin:$PATH"
   ```
2. **Clone the repository**:
   ```bash
   git clone https://github.com/fahmiaziz98/10-11-ml-model-serving.git
   cd 10-11-ml-model-serving
   ```
3. **Set up virtual env**
   ```bash
   uv venv .venv
   source .venv/bin/activate
   ```
4. **Install dependency**
   ```bash
   uv pip install -r requirements.txt
   ```
5. **Set Environment variable**
   ```bash
   cp .env.example .env
   ```
6. **Run API locally**
   ```bash
   make run-api
   ```
   The API will be available at **http://127.0.0.1:7860/docs**
7. **Run Streamlit UI**
   ```bash
   make run-streamlit
   ```
The Streamlit interface will be available at **http://localhost:8501**

## Docker Usage

1. **Build Docker Image**
   ```bash
   make docker-build
   ```

2. **Run Docker Container**
   ```bash
   make docker-run
   ```
Once running, the API will be accessible at **http://localhost:7860/docs**

3. **Clean Docker Container**
   ```bash
   make docker-clean
   ```
This stops and removes the container named `ml-model-serving-container`.

## Load Testing with Locust

1. Start Locust:
   ```bash
   make run-locust
   ```

2. Open your browser and go to:
**http://localhost:8089**

3. Enter the number of users, spawn rate, and target host (e.g., `http://localhost:7860`), then click **Start swarming**.

---


## Load Testing with Locust
API load testing has been performed using Locust to evaluate the performance and scalability of the endpoints. For detailed instructions and results, please refer to the [Documentation](locust.md).

## Deploy API via HuggingFace Spaces (Recommended)
For a step-by-step guide on deploying applications on HuggingFace Spaces, please visit [Deploy Applications on HuggingFace Spaces](https://huggingface.co/blog/HemanthSai7/deploy-applications-on-huggingface-spaces)