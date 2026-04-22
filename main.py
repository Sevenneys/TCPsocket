import socket
import platform
import os

from tcp_socket import *

oc = platform.system()
if oc.lower() == "windows":
    os.system("cls")
elif oc.lower() == "linux":
    os.system("clear")

print(f"\n[1] MODE-SERVER (Принять);")
print(f"[2] MODE-CLIENT (Отправить);")

data_in = input(f"\n{os.getlogin()}: ")

print(f"\n[1] TYPE-DATA STRING")
print(f"[2] TYPE-DATA FILE")

data_in_type = input(f"\n{os.getlogin()}: ")

if data_in == "1":
    server_socket(data_in_type)
elif data_in == "2":
    client_socket(data_in_type)

