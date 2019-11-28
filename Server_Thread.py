#!/usr/bin/env python3
import socket
from _thread import *

gDict = {}
newDict = {}

# receive function
def receive(c):
    data = c.recv(1024)
    newDict[c] = data.decode("ascii") #First message contains Username

    while True:
        # data received from client
        data = c.recv(1024)

        if not data or data == 'quit':
            print('Bye')
            print(f"{gDict.pop(c)} Has disconnected")
            # lock released on exit
            # print_lock.release()
            exit_thread()
            break
        broadcast(c, data.decode("ascii"))

    c.close()


def broadcast(c, data):
    print(" | ".join(str(i) for i in gDict.values()))

    for connection in gDict:
        message = f"{newDict[c]} > {data}"
        connection.send(f"{newDict[c]} > {data}".encode("ascii"))
        #connection.send(message)
        print(f"Connection: {gDict.get(connection)} | Data: {data}")
        print(f"{newDict[c]} > {data}")


def main():
    #Local host: '127.0.0.1'
    host = '127.0.0.1'
    port = 42069
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        conn, addr = s.accept()
        global gDict
        global newDict
        # Adds Socket / Connection to Dict
        gDict[conn] = addr

        print('Connected to :', addr[0], ':', addr[1])

        # receive(conn)
        start_new_thread(receive, (conn,))

        #Keyboardinterrupt with CTRL + C, make sure to close active clients first

    # We never reach this line but it feels good to have it
    s.close()
    quit()


"""
    If this file is called directly as a python program 
    Main() will be called. 
    If it's included as a library nothing will be executed 
	since all code is located in functions.
"""

if __name__ == '__main__':
    main()
