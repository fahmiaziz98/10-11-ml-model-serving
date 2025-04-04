import os
import requests
import streamlit as st
from scripts.s3 import upload_image_to_s3


API_URL = "https://fahmiaziz-ml-model-restapi.hf.space/api/v1/"
headers = {
  'Content-Type': 'application/json'
}

st.title("ML Model Serving Over REST API")

model = st.selectbox(
    "Select Model",
    [
        "Sentiment Classifier", 
        "Disaster Classifier", 
        "Pose Classifier"
    ]
)

if model=="Sentiment Classifier":
    text = st.text_area("Enter Your Movie Review")
    user_id = st.text_input("Enter user id", "123vb")
    data = {"text": [text], "user_id": user_id}
    model_api = "sentiment_classification"

elif model=="Disaster Classifier":
    text = st.text_area("Enter Your Disaster News")
    user_id = st.text_input("Enter user id", "123vb")
    data = {"text": [text], "user_id": user_id}
    model_api = "disaster_classification"

elif model == "Pose Classifier":
    select_file = st.radio("Select the image source", ["Local", "URL"])
    url = None  

    if select_file == "URL":
        url = st.text_input("Enter Your Image URL")
    
    else:
        image = st.file_uploader("Upload the image", type=["jpg", "jpeg", "png"])
        if image is not None:
            file_name = "images/temp.jpg"
            os.makedirs(os.path.dirname(file_name), exist_ok=True)
            with open(file_name, "wb") as f:
                f.write(image.read())
            url = upload_image_to_s3(file_name)

    if url:
        data = {"url": [url], "user_id": "123vb"}
        model_api = "image_classification"
    else:
        st.warning("Please provide a valid image URL or upload an image.")


if st.button("Predict"):
    with st.spinner("Predicting... Please wait!!!"):
        response = requests.post(API_URL+model_api, headers=headers,
                                 json=data)
        
        output = response.json()

    st.write(output)