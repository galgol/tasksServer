#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

#options for client to choose from
menu_bar = { 1:"show all options for availble tasks",2: "create a new option for a task" , 3:"insert a new task to TODO list", 4:"delete a task from TODO list", 5:"edit a task (in available options)" , 6:"print all TODO list", 7:"exit"}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    chosen_action = '0' #deafult to start
    while chosen_action != '7': #didnt request to exit
        for i,j in menu_bar.items(): #prints menu to client
            print(i,j)
        chosen_action = input("choose what to do ")
        if chosen_action == '1':
            print("all options for availble tasks are: ")
            s.sendall(bytes(chosen_action, 'utf-8'))
            data = s.recv(1024)
            print('Received task to server\n', data)
        elif chosen_action == '2':
            task = input("insert a new available task ") #requested to insert so get what to insert
            s.sendall(bytes(chosen_action +' ' + task,'utf-8')) #sends to server the action to enter to db to list_of_tasks table
            data = s.recv(1024) #returned action
            print('Received task to server\n', data)
        elif chosen_action == '3':
            task = input("insert the new task to TODO list") #requested to insert so get what to insert
            s.sendall(bytes(chosen_action +' ' + task,'utf-8')) #sends to server the action to enter to db to tasks table
            data = s.recv(1024) #returned action
            print('Received task to server\n', data)
        elif chosen_action == '4': #requested to delete so get what to delete
            task = input("insert the task you want to delete from TODO list")
            s.sendall(bytes(chosen_action +' ' + task, 'utf-8')) #sends to server the action to delete from db from tasks table
            data = s.recv(1024) #returned action
            print('Received task to server\n', data)
        elif chosen_action == '5':
            old_task = input("insert the task ID you want to update (in available options)")
            new_task = input("insert new description of task (to available options)")
            s.sendall(bytes(chosen_action + ' ' + old_task + '#' + new_task, 'utf-8')) # the '#' helps distingush old and new
            data = s.recv(1024)
            print('Received task to server\n', data)
        elif chosen_action == '6':
            print("all tasks in TODO list are: ")
            s.sendall(bytes(chosen_action, 'utf-8'))
            data = s.recv(1024)
            print('Received task to server\n', data)
        else:
            break
    #closing - requested to exit
    s.sendall(bytes(chosen_action, 'utf-8'))
    data = s.recv(1024)
    print('closing \n', data)