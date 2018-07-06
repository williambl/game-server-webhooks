import netifaces as ni
import subprocess

game = ""
image = ""

ni.ifaddresses('eth0')
ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

subprocess.run(["python3", "push-webhook.py", "--game", game, "--link", f"http://{ip}:8080", "--addr", ip, "--image", image])
