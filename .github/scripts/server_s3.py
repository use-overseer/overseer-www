import os
import boto3
from botocore.config import Config

s3 = boto3.client(
    "s3",
    region_name=os.getenv("SERVER_REGION", "us-east-1"),
    endpoint_url=os.getenv("SERVER_ENDPOINT"),
    aws_access_key_id=os.getenv("SERVER_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SERVER_SECRET_KEY")
)

BUCKET = os.getenv("SERVER_BUCKET")

# List files
response = s3.list_objects_v2(Bucket=BUCKET)
for obj in response.get("Contents", []):
    print(obj["Key"])

# Upload a file
s3.put_object(
    Bucket=BUCKET,
    Key="example.txt",
    Body="Hello, this is a sample file content."
)

# Download a file
response = s3.get_object(
    Bucket=BUCKET,
    Key="example.txt"
)
content = response["Body"].read().decode("utf-8")
print("Downloaded content:", content)

# Delete files
s3.delete_objects(
    Bucket=BUCKET,
    Delete={
        "Objects": [
            {"Key": "example.txt"},
            {"Key": "another_file.txt"}
        ]
    }
)
