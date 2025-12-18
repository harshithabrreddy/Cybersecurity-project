import socket
hostname = input("Enter hostname or IP address: ")
print("You entered:", hostname)
ip_address = socket.gethostbyname(hostname)
print("IP Address is:", ip_address)