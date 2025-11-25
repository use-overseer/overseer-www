import os
import requests
from pathlib import Path

BASE_URL = os.getenv("BASE_URL")
API_TOKEN = os.getenv("API_TOKEN")

def upload_file(local_path: Path, key: str):
    if not BASE_URL:
        raise RuntimeError("Missing BASE_URL environment variable.")
    if not API_TOKEN:
        raise RuntimeError("Missing API_TOKEN environment variable.")

    url = f"{BASE_URL.rstrip('/')}/{key.lstrip('/')}"

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "text/markdown"
    }

    with local_path.open("rb") as f:
        content = f.read()

    response = requests.put(url, data=content, headers=headers)
    if not response.ok:
        raise RuntimeError(
            f"Upload failed for {key}: {response.status_code} - {response.text}"
        )

    print(f"✔ Uploaded: {key} → {url}")

def main():
    root = Path("public-content/")
    if not root.exists():
        raise RuntimeError("Directory public-content/ does not exist.")

    for file in root.rglob("*.md"):
        rel_path = file.relative_to(root)
        key = f"{rel_path.as_posix()}"
        upload_file(file, key)

if __name__ == "__main__":
    main()
