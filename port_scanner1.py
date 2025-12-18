import socket

target = input("Enter target hostname or IP: ")

try:
    target_ip = socket.gethostbyname(target)
    print("Target IP:", target_ip)
except socket.gaierror:
    print("Invalid hostname")
    exit()


