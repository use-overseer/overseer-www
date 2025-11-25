import os
import requests

BUCKET_URL = os.getenv("SERVER_BUCKET_URL")
ACCESS_KEY = os.getenv("SERVER_ACCESS_KEY")
SECRET_KEY = os.getenv("SERVER_SECRET_KEY")

PUBLIC_DIR = "public-content"

def upload_file(path, key):
    with open(path, "rb") as f:
        content = f.read()

    url = f"{BUCKET_URL}/{key}"
    headers = {
        "Authorization": f"Bearer {ACCESS_KEY}:{SECRET_KEY}",
        "Content-Type": "text/markdown"
    }

    r = requests.put(url, data=content, headers=headers)

    if r.status_code not in [200, 201]:
        print(f"Error subiendo {key}: {r.status_code} -> {r.text}")
    else:
        print(f"Subido correctamente: {key}")

def main():
    for root, _, files in os.walk(PUBLIC_DIR):
        for file in files:
            if file.endswith(".md"):
                local_path = os.path.join(root, file)
                key = file  
                upload_file(local_path, key)

if __name__ == "__main__":
    main()
