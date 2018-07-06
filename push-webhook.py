import requests

url = ""

name = "A name"
game = "A game"
addr = "0.0.0.0"

request = {
    "text": "New server started!",
    "attachments": [
        {
            "fallback": "New "+game+" server started on "+addr,
            "author_name": name,
            "title": "New "+game+" server started!",
            "text": "Address: "+addr
        }
    ]
}

r = requests.post(url, json = request)
