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

 # find the game in the game list, and return the image that corresponds to it
def set_game_image(game_list, game_name):
    return game_list.get(game_name, "")

 # get the ip address from eth0
def get_ip_address():
    ni.ifaddresses('eth0')
    return ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

 # create the json request
def create_request(game, message, image, ip):
    request = {
        "text": "New server started!",
        "attachments": []
    }

    attachment = {
        "fallback": f"New {game} server started at {ip}.",
        "title": f"{game} server started!",
        "text": f"{message}",
        "color": "#fa8423",
        "fields": [],
        "image_url": f"{image}"
    }

    fields = [
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
    ]

    for field in fields:
        attachment['fields'].append(field)

    request['attachments'].append(attachment)
    print(request)
    return request

def main():
    url, game, redirect, message, games = setup_variables()
    image = set_game_image(games, game)
    ip = get_ip_address()

    request = create_request(game, message, image, ip)
    r = requests.post(url, json = request)

if __name__ == "__main__":
    main()
