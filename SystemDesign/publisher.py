# a publisher

import socket

TCP_IP = '127.0.0.1'  # localhost
TCP_PORT = 65432      # non-privileged ports are > 1023
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

     s.bind((TCP_IP, TCP_PORT))
     s.listen()
     conn, addr = s.accept()
     with conn:
         print(f"Connected by cleint: {addr}")
         while True:
             data = conn.recv(BUFFER_SIZE)
             if not data:
                 break
             conn.sendall(data)
            
