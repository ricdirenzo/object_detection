import requests
from constants import URL, KEY, CLASS


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
