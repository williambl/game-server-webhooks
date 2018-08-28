import netifaces as ni
import subprocess
import sys

game = sys.argv[1]

if (game == "Garry's Mod Sandbox"):
    image = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Gmodlogo.svg/480px-Gmodlogo.svg.png"
elif (game == "Garry's Mod Battle Royale"):
    image = "https://steamuserimages-a.akamaihd.net/ugc/279595726542479855/0FA7121E5843B345BC171845C3FB2D80BC13758D/"
elif (game == "Garry's Mod Jazzstronauts"):
    image = "https://steamuserimages-a.akamaihd.net/ugc/946206517762697863/E7057CE35109733B7AA11BE7EAF677F5CE6BB7B4/"
elif (game == "Minecraft"):
    image = "https://www.planwallpaper.com/static/images/YkeGu-ph_rawmmx5.png"
elif (game == "Left 4 Dead 2"):
    image = "https://orig02.deviantart.net/e37a/f/2010/277/0/1/left_4_dead_2_ellis_by_jasperhalegirl-d3024kj.jpg"
elif (game == "Team Fortress 2"):
    image = "http://clipground.com/images/team-fortress-2-clipart-6.png"
else:
    image = ""

ni.ifaddresses('eth0')
ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

subprocess.run(["python3.6", "push-webhook.py", "--game", game, "--link", f"http://{ip}:8080", "--addr", ip, "--image", image])
subprocess.run(["python3.6", "redirect-to-game.py", ip])
