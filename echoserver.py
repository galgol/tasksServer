#!/usr/bin/env python3

import socket
import main
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

'''
creates a socket object that supports the context manager type,
 so you can use it in a with statement. There’s no need to call s.close()
'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        main.create_db()
        while True:
            data = conn.recv(1024)
            if not data:
                break
            main.insert_db(data)
            conn.sendall(data)

