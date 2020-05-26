import os
import socket


def server_run():
    server_addr = '/tmp/uds_server.sock'

    if os.path.exists(server_addr):
        os.unlink(server_addr)

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(server_addr)
    sock.listen(0)

    print('Server ready.')

    size = 1 << 20
    conn, _ = sock.accept()
    while True:
        conn.recv(size)
        conn.send("Hello there!".encode('utf-8'))


if __name__ == '__main__':
    server_run()
