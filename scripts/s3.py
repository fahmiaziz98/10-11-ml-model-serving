import os
import boto3
from utils.log import logger
from dotenv import load_dotenv
load_dotenv()


aws_access_key = os.getenv("AWS_ACCESS_KEY_ID") 
aws_key_pw =  os.getenv("AWS_SECRET_ACCESS_KEY") 
BUCKET_NAME =  os.getenv("BUCKET_NAME") 


s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_key_pw,    
)

def download_model_from_s3(local_path: str, s3_prefix: str):
    try:
        if os.path.exists(local_path) and os.listdir(local_path):
            logger.info(f"Model {local_path} already exists. Skipping download.")
            return

        logger.info(f"Downloading model from S3: {s3_prefix} to {local_path}")
        os.makedirs(local_path, exist_ok=True)
        paginator = s3.get_paginator("list_objects_v2")

        for result in paginator.paginate(Bucket=BUCKET_NAME, Prefix=s3_prefix):
            if "Contents" in result:
                for key in result["Contents"]:
                    s3_key = key["Key"]
                    local_file = os.path.join(local_path, os.path.relpath(s3_key, s3_prefix))
                   
                    os.makedirs(os.path.dirname(local_file), exist_ok=True)
                    s3.download_file(BUCKET_NAME, s3_key, local_file)
                    logger.info(f"Completed download {s3_key} to {local_file}")
    except Exception as e:
        logger(f"Failed to download model from S3: {e}")
        raise RuntimeError(f"Error downloading model from S3: {e}")

def upload_image_to_s3(
        file_name, 
        s3_prefix="ml-images", 
        object_name=None
    ):
    if object_name is None:
        object_name = os.path.basename(file_name)

    object_name = f"{s3_prefix}/{object_name}"
    s3.upload_file(file_name, BUCKET_NAME, object_name)
    logger.info(f"Uploaded {file_name} to s3://{BUCKET_NAME}/{object_name}")

    response = s3.generate_presigned_url(
        'get_object',
        Params={
            "Bucket": BUCKET_NAME,
            "Key": object_name
        },
        ExpiresIn=3600
    )
    logger.info(f"Generated presigned URL for {object_name}: {response}")
    return response