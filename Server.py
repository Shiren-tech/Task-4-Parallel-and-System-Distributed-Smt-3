import socket 
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = "127.0.0.1"
server_port = 12345

server_socket.bind((server_ip, server_port))
server_socket.listen()

print("Server is waiting for a client...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected by {client_address}")


    while True:
        data = client_socket.recv(1024)

        if not data:
            break

        message = data.decode("utf-8")
        print(f"Message received: {message}")

        response = "Message received"
        client_socket.sendall(response.encode("utf-8"))

    client_socket.close()
    time.sleep(1)