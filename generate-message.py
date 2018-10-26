from http.server import *
from redirect import FakeRedirect
import netifaces as ni
import subprocess
import sys
import json
import requests
import argparse
import os

 # set up variables from input
def setup_variables():
    url = os.getenv("GAME_WEBHOOK_URL")

    game = sys.argv[1]
    redirect = "redirect" in sys.argv
    message = sys.argv[3]

    with open("games.json", "r") as f:
        games = json.load(f)

    return url, game, redirect, message, games

def set_game_image(game_list, game_name):
    return game_list.get(game_name, "")

def get_ip_address():
    ni.ifaddresses('eth0')
    return ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

def set_link(redirect):
    if (redirect):
        return f"http://{ip}:8080"
    else:
        return ""

def create_request(url, game, message, image, ip):
    request = {
        "text": "New server started!",
        "attachments": [
            {
                "fallback": f"New {game} server started at {ip}.",
                "title": f"{game} server started!",
                "title_link": f"{url}",
                "text": f"{message}",
                "color": "#fa8423",
                "fields": [
                    {
                        "title": "Game",
                        "value": f"{game}",
                        "short": True
                    },
                    {
                        "title": "Address",
                        "value": f"{ip}",
                        "short": True
                    }
                ],
                "actions": [
                    {
                        "name": "Join Game",
                        "text": "Join",
                        "url": f"{url}",
                        "style": "primary"
                    }
                ],
                "image_url": f"{image}"
            }
        ]
    }
    return request

def main():
    url, game, redirect, message, games = setup_variables()
    image = set_game_image(games, game)
    ip = get_ip_address()
    link = set_link(redirect)

    request = create_request(url, game, message, image, ip)
    r = requests.post(url, json = request)

    if (redirect):
        HTTPServer(("", 8080), FakeRedirect).serve_forever()

if __name__ == "__main__":
    main()
