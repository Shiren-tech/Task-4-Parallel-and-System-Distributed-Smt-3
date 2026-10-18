import socket

server_ip = "127.0.0.1"
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_ip, server_port))

while True:
    message = input("Enter a message (type 'exit' to quit): ")

    if message.lower() == "exit":
        break

    client_socket.send(message.encode("utf-8"))

    response = client_socket.recv(1024).decode("utf-8")
    print(f"Server response: {response}")

client_socket.close()