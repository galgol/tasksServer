#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

menu_bar = {1:"insert a new task", 2:"delete a task", 3:"edit a task" , 4:"print all tasks", 5:"exit"}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    chosen_action = '0'
    while chosen_action != '5':
        for i,j in menu_bar.items():
            print(i,j)
        chosen_action = input("choose what to do ")
        if chosen_action == '1':
            task = input("insert the new task ")
            s.sendall(bytes(chosen_action +' ' + task,'utf-8'))
            data = s.recv(1024)
            print('Received task to server\n', data)
        elif chosen_action == '2':
            task = input("insert the task you want to delete ")
            s.sendall(bytes(chosen_action +' ' + task, 'utf-8'))
            data = s.recv(1024)
            print('Received task to server\n', data)
        elif chosen_action == '3':
            old_task = input("insert the task you want to change ")
            new_task = input("insert new task ")
            s.sendall(bytes(chosen_action + ' ' + old_task + '#' + new_task, 'utf-8'))
            data = s.recv(1024)
            print('Received task to server\n', data)
        elif chosen_action == '4':
            print("all tasks are: ")
            s.sendall(bytes(chosen_action, 'utf-8'))
            data = s.recv(1024)
            print('Received task to server\n', data)
        else:
            break
    #closing
    s.sendall(bytes(chosen_action, 'utf-8'))
    data = s.recv(1024)
    print('closing \n', data)