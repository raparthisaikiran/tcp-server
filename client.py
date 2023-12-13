import socket

# Create client socket.
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server (replace 127.0.0.1 with the real server IP).
client_sock.connect(('127.0.0.1', 6544))
message = ''

while message != 'X':
    # take inout from user
    message = input()
    arr = bytes(message, 'utf-8')
    # Send some data to server.
    client_sock.sendall(arr)

    # Receive some data back.
    # chunks = []
    # while True:
    #     data = client_sock.recv(2048)
    #     if not data:
    #         break
    #     chunks.append(data)
    # print('Received', repr(b''.join(chunks)))

    # Disconnect from server.
    # client_sock.close()

# Disconnect from server.
client_sock.close()
client_sock.shutdown(socket.SHUT_WR)

