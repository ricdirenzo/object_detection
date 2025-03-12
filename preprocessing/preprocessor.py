import os
from dotenv import load_dotenv
import requests
from constants import URL, CLASS

load_dotenv()

# secrets
KEY = os.getenv("KEY")

def get_image_urls(num: int) -> list:
    try:
        resp = requests.get(
            url=URL,
            params={
                'query': CLASS,
                'per_page': num
            },
            headers={'Authorization': KEY}
        )
        data = resp.json()
        return [img['src']['original'] for img in data['photos']]
    except Exception as e:
        print(e)
