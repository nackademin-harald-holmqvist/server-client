#!/usr/bin/env python3

import socket
from _thread import *


def receive_from_server(s):
    while True:
        data = s.recv(1024)
        if data:
            print('\n', data.decode("ascii"))

def main():
    # local host IP '127.0.0.1'
    #host = '172.20.201.124'
    host = '127.0.0.1'
    port = 42069

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("Connected to Server: ", s.getsockname())

    username = input("Username: ")
    s.send(username.encode('ASCII'))

    while True:
        start_new_thread(receive_from_server, (s, ))

        message = input('\nGive a new text or ["quit"] or <RETURN>] to quit: ')
        s.send(message.encode('ASCII'))

        if message == 'quit' or message == '':
            print("Client Exiting program ...")
            exit_thread()
            break

        print(f"{username} > {type(message)}")

    s.shutdown()
    s.close()
    quit()


if __name__ == '__main__':
    main()
