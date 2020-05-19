def client_run():
    import socket
    import time

    server_addr = '/tmp/uds_server.sock'

    duration = 1
    end = time.time() + duration
    msgs = 0

    print('Receiving messages...')

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(server_addr)
    while time.time() < end:
        sock.send("Hello there!".encode('utf-8'))
        data = sock.recv(32)
        msgs += 1
    sock.close()

    print('Received {} messages in {} second(s).'.format(msgs, duration))


if __name__ == '__main__':
    client_run()
