import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 9999))

print("UDP Server is running...")

while True:
    data, addr = server.recvfrom(1024)
    print("Message from client:", data.decode())

    server.sendto("Message received".encode(), addr)