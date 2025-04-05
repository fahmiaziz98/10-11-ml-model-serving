# Run API locally
run-api:
    uvicorn app:app --host 0.0.0.0 --port 7860

# Run streamlit app
run-streamlit:
	streamlit run streamlit_app.py
	
# Run Locust for load testing
run-locust:
    locust -f api_testing/locustfile.py

# Build Docker image
docker-build:
    docker build -t ml-model-serving .

# Run API in Docker
docker-run:
    docker run -p 7860:7860 --name ml-model-serving-container ml-model-serving

# Stop and remove Docker container
docker-clean:
    docker stop ml-model-serving-container || true && docker rm ml-model-serving-container || true