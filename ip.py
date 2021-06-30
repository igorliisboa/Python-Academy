#Checando o endereço IP

import socket
import requests

ip_local = socket.gethostbyname(socket.gethostname())
print(f"IP local: {ip_local}")

ip_publico = requests.get('http://api.ipify.org').text
print(f"IP público: {ip_publico}")