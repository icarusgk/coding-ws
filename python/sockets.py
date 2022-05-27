import socket

# ? creating the socket
hostname = '127.0.0.1'
# As a port, we can use any number in the range from 0 to 65535.
port = 8080
# Create a tuple
address = (hostname, port)

client_socket = socket.socket()

# ? connecting to the server
client_socket.connect(address)

# An important note: what you send through your socket must be 
# necessarily in binary format.

data = 'Wake up, Neo'
# ? converting to bytes
# Converting to bytes
data = data.encode()
print(data)
data = data.decode()
print(data)


# ? converting to bytes
# Sending through socket
client_socket.send(data)


# * Receiving data
# the recv() method requires a buffer size as an argument
# an integer argument specifying the maximum number of bytes 
# to be received at once.

# ? receiving the response
response = client_socket.recv(1024)

# ? decoding from bytes to string
response = response.decode()
print(response)

# Once we're done, we simply end the connection with close()
client_socket.close()