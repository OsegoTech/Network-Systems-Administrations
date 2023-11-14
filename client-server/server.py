import socket

# define server IP Address and port
server_ip = '127.0.0.1'
server_port = 12345

# create socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind server to the IP address and port
server.bind((server_ip, server_port))

# listening to incoming connections
server.listen(1)

print('Server is listening to incoming connection....')

while True:

    #Accept a client connection
    client, addr = server.accept()

    # Receive data from the client
    data = client.recv(1024).decode()
    print(f"Received from the client: {data}")

    # process the client's request
    response = f"Server received: {data}"

    # send response back to the client
    client.send(response.encode())

    # close the client connection
    client.close()