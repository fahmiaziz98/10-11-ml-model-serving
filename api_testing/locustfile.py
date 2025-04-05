import os
import json
import random
from locust import HttpUser, constant_pacing, task


def load_json_file(file_path: str) -> list:
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise ValueError(f"Invalid JSON format in {file_path}. Expected a list.")
            return data
    except Exception as e:
        print(f"Error loading JSON file {file_path}: {e}")
        return []


DISASTER = load_json_file(
    os.path.join(os.path.dirname(__file__), "sample_data/disaster.json")
)

SENTIMENT = load_json_file(
    os.path.join(os.path.dirname(__file__), "sample_data/sentiment.json")
)

IMAGE = load_json_file(
    os.path.join(os.path.dirname(__file__), "sample_data/image.json")
)

class LoadTestSentiment(HttpUser):    
    wait_time = constant_pacing(1) # second
    
    @task
    def post_sentiment(self):
        comment = random.choice(SENTIMENT)
        self.client.post("/sentiment_classification", json=comment)
    
    @task
    def post_disaster(self):
        tweet = random.choice(DISASTER)
        self.client.post("/disaster_classification", json=tweet)

    @task
    def post_image_clf(self):
        image = random.choice(IMAGE)
        self.client.post("/image_classification", json=image)