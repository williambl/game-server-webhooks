import requests

url = ""

request = {
    "text": "text",
    "attachments": [
        {
            "fallback": "fallback",
            "author_name": "author_name",
            "title": "title",
            "text": "text"
        }
    ]
}

r = requests.post(url, json = request)
