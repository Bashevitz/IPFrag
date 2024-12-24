import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 55555))

print("UDP Server is listening on port 55555...")

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Received message from {addr}: {data.decode('utf-8')}")
