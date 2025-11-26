import os
import boto3
from botocore.config import Config

BUCKET = os.getenv("SERVER_BUCKET")
ENDPOINT = os.getenv("SERVER_ENDPOINT")
REGION = os.getenv("SERVER_REGION")
ACCESS_KEY = os.getenv("SERVER_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("SERVER_SECRET_ACCESS_KEY")

PUBLIC_DIR = "public-content"


def get_s3_client():
    if not all([BUCKET, ENDPOINT, REGION, ACCESS_KEY, SECRET_KEY]):
        raise RuntimeError("Faltan variables de entorno para conectar al bucket")

    return boto3.client(
        "s3",
        region_name=REGION,
        endpoint_url=ENDPOINT,
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        config=Config(signature_version="s3v4")
    )


def upload_file(path, key, s3):
    with open(path, "rb") as f:
        content = f.read()

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=content,
        ContentType="text/markdown"
    )

    print(f"✓ Subido: {key}")


def main():
    s3 = get_s3_client()

    for root, _, files in os.walk(PUBLIC_DIR):
        for file in files:
            if file.endswith(".md"):
                local_path = os.path.join(root, file)

                # Mantiene estructura de carpetas dentro del bucket
                rel_path = os.path.relpath(local_path, PUBLIC_DIR)
                key = rel_path.replace("\\", "/")

                upload_file(local_path, key, s3)


if __name__ == "__main__":
    main()
