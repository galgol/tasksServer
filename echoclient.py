#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("please enter your new to-do task\n")
    task = input()
    s.sendall(bytes(task,'utf-8'))
    data = s.recv(1024)

    print('Received task to server\n', repr(data))