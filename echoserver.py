#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

'''
creates a socket object that supports the context manager type,
 so you can use it in a with statement. There’s no need to call s.close()
'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #. AF_INET is the Internet address family for IPv4 , SOCK_STREAM is the socket type for TCP
    #the protocol that will be used to transport our messages in the network
    s.bind((HOST, PORT)) #associate the socket with a specific network interface and port number
    #the values of bind depend on the address family - IPv4 has 2
    # host could be a hostname, IP address or empty string.
    s.listen() # enables a server to accept() connections
    #listen() has a backlog parameter. It specifies the number of unaccepted connections
    # that the system will allow before refusing new connections
    #If your server receives a lot of connection requests simultaneously, increasing the backlog value
    # may help by setting the maximum length of the queue for pending connections
    conn, addr = s.accept() #accept() blocks and waits for an incoming connection
    #When a client connects, it returns a new socket object representing the connection and
    # a tuple holding the address of the client , The tuple will contain (host, port) for IPv4 connections
    #now we have a new socket object from accept()
    #it’s the socket that you’ll use to communicate with the client. It’s distinct from the listening socket that
    # the server is using to accept new connections
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

    '''
    After getting the client socket object conn from accept(), an infinite while loop is used to loop 
    over blocking calls to conn.recv(). This reads whatever data the client sends and echoes it back 
    using conn.sendall().
    If conn.recv() returns an empty bytes object, b'', then the client closed the connection and 
    the loop is terminated. 
    The with statement is used with conn to automatically close the socket at the end of the block
    '''