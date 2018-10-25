import netifaces as ni
import subprocess
import sys
import json

game = sys.argv[1]
message = sys.argv[3]

if (len(sys.argv) > 2):
    redirect_to_game = sys.argv[2] == "redirect"
else:
    redirect_to_game = False

with open("games.json", "r") as f:
    games = json.load(f)

image = games.get(game, "")

ni.ifaddresses('eth0')
ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

if (redirect_to_game):
    link = f"http://{ip}:8080"
else:
    link = ""

process = ["python3.6", "push-webhook.py", "--game", game, "--link", link, "--addr", ip, "--image", image]
if (message != None):
    process.append("--message")
    process.append(message)

subprocess.run(process)

if (redirect_to_game):
    subprocess.run(["python3.6", "redirect-to-game.py", ip])
