import socket

# define the server IP address and port
server_ip = '127.0.0.1'
server_port = 123`45

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client.connect((server_ip, server_port))
print(f"Connected to server at {server_ip}: {server_port}")

# send request to the server
message = 'Hello , Server!'
client.send(message.encode())

# receive the server response
response = client.recv(1024).decode()
print(f"Server response: {response}")

client.close()