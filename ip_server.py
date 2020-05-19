#!/usr/bin/env python

import socket


def server_run():
    server_addr = '127.0.0.1'
    server_port = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((server_addr, server_port))
    sock.listen(0)

    size = 1 << 20
    data = b'0' * size
    print('Server ready.')

    conn, _ = sock.accept()
    while True:
        data = conn.recv(32)
        conn.send("Hello there!".encode('utf-8'))


if __name__ == '__main__':
    server_run()
