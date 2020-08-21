import os
import socket

unix_socket_name = 'unix.sock'
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

if os.path.exists(unix_socket_name):
    os.remove(unix_socket_name)

sock.bind(unix_socket_name)

while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
    else:
        print('Message', result.decode('utf-8'))