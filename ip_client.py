import socket
import time


def client_run():
    server_addr = '127.0.0.1'
    server_port = 5000

    duration = 1
    end = time.time() + duration
    msgs = 0

    print('Receiving messages...')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_addr, server_port))
    while time.time() < end:
        sock.send("Hello there!".encode('utf-8'))
        data = sock.recv(32)
        msgs += 1
    sock.close()

    print('Received {} messages in {} second(s).'.format(msgs, duration))


if __name__ == '__main__':
    client_run()
