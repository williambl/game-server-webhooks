import requests
import argparse
import os

url = os.getenv("GAME_WEBHOOK_URL")

parser = argparse.ArgumentParser()

parser.add_argument("--game", help="The name of the game being played.", required=True)
parser.add_argument("--link", help="A link to the game being played.", required=True)
parser.add_argument("--addr", help="The address of the server.", required=True)
parser.add_argument("--image", help="An image of the game.", required=True)
parser.add_argument("--message", help="The message to send", required=False)
args = parser.parse_args()

game = args.game
link = args.link
addr = args.addr
image = args.image
message = args.message

request = {
    "text": "New server started!",
    "attachments": [
        {
            "fallback": f"New {game} server started at {addr}.",
            "title": f"{game} server started!",
            "title_link": f"{link}",
            "text": f"{message}"
            "color": "#fa8423",
            "fields": [
                {
                    "title": "Game",
                    "value": f"{game}",
                    "short": True
                },
		{
		    "title": "Address",
		    "value": f"{addr}",
                    "short": True
		}
            ],
            "actions": [
                {
                    "name": "Join Game",
                    "text": "Join",
                    "url": f"{link}",
                    "style": "primary"
                }
            ],
            "image_url": f"{image}"
        }
    ]
}
r = requests.post(url, json = request)
