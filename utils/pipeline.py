import torch
from transformers import pipeline, AutoImageProcessor

# Set the device to GPU if available, otherwise use CPU
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

def load_model(local_path, is_image_model=False):
    """
    Load a model from the specified local path.
    
    Args:
        local_path (str): The local path to the model.
        is_image_model (bool): Flag indicating if the model is an image model.
    Returns:
        pipeline: The loaded model pipeline.
    """
    if is_image_model:
        image_processor = AutoImageProcessor.from_pretrained(local_path, use_fast=True)
        return pipeline("image-classification", model=local_path, device=device, image_processor=image_processor)
    return pipeline("text-classification", model=local_path, device=device)