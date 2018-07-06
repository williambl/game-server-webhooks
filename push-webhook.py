import requests
import argparse

url = ""

parser = argparse.ArgumentParser()

parser.add_argument("--game", help="The name of the game being played.", required=True)
parser.add_argument("--link", help="A link to the game being played.", required=True)
parser.add_argument("--addr", help="The address of the server.", required=True)
parser.add_argument("--image", help="An image of the game.", required=True)
args = parser.parse_args()

game = args.game
link = args.link
addr = args.addr
image = args.image

request = {
    "text": "New server started!",
    "attachments": [
        {
            "fallback": f"New {game} server started at {addr}",
            "title": f"{game} server started!",
            "title_link": f"{link}",
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
