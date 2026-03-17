import socket

target = "127.0.0.1"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((target, port))
    print("Connection successful")
except:
    print("Connection failed")

s.close()