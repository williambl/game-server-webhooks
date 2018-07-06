import requests

url = ""

game = "A game"
link = "https://example.com"
addr = "0.0.0.0"
image = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Example_image.svg/1024px-Example_image.svg.png"

request = {
    "text": "New server started!",
    "attachments": [
        {
            "fallback": f"New {game} server started at {addr}",
            "title": f"{game} server started!",
            "title_link": f"{link}",
            "text": f"Address: "+addr,
            "color": "#fa8423",
            "fields": [
                {
                    "title": "Game",
                    "value": f"{game}"
                },
		{
		    "title": "Address",
		    "value": f"{addr}"
		}
            ],
            "image_url": f"{image}",
        }
    ]
}
r = requests.post(url, json = request)
