#!/usr/bin/env python3

import socket
import main
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on

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
        main.create_db() #create initial DB: dbtest
        while True:
            data = conn.recv(1024)
            if not data:
                break
            rec_data = data.decode() #get request from client according to menu bar
            if rec_data[0] == '1':
                main.insert_db(data)
                conn.sendall(data)
            elif rec_data[0] == '2':
                main.delete_from_db(data)
                conn.sendall(data)
            elif rec_data[0] == '3':
                main.update_record_table(data)
                conn.sendall(data)
            elif rec_data[0] == '4':
                main.print_all_table()
                conn.sendall(data)
            elif rec_data[0] == '5':
                main.close_all()
                conn.sendall(data)
            else:
                break