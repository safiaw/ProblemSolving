# a subscriber

import socket

TCP_IP = '127.0.0.1'  # localhost
TCP_PORT = 65432      # non-privileged ports are > 1023
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

     s.connect((TCP_IP, TCP_PORT))
     s.sendall(b"Hello, world")
     data = s.recv(BUFFER_SIZE)

print(f"Received: {data!r}")
            
