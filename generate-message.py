import netifaces as ni
import subprocess
import sys

game = sys.argv[1]

if (game == "Garry's Mod Sandbox"):
    image = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Gmodlogo.svg/480px-Gmodlogo.svg.png"
elif (game == "Garry's Mod Battle Royale"):
    image = "https://steamuserimages-a.akamaihd.net/ugc/279595726542479855/0FA7121E5843B345BC171845C3FB2D80BC13758D/"
else:
    image = ""

ni.ifaddresses('eth0')
ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

subprocess.run(["python3.6", "push-webhook.py", "--game", game, "--link", f"http://{ip}:8080", "--addr", ip, "--image", image])
subprocess.run(["python3.6", "redirect-to-game.py", ip])
