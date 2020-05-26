import posix_ipc
import mmap
import os
import time


def client_run():
    memory = posix_ipc.SharedMemory("pyflink")
    client_semaphore = posix_ipc.Semaphore("client")
    server_semaphore = posix_ipc.Semaphore("server")
    map_file = mmap.mmap(memory.fd, memory.size)
    size = (1 << 20) + 1
    duration = 10
    end = time.time() + duration
    msgs = 0
    while time.time() < end:
        server_semaphore.acquire()
        map_file.seek(0)
        data = map_file.read(size)
        while data[-1] != 49:
            map_file.seek(0)
            data = map_file.read(size)
        # print(data[-2:-1])
        client_semaphore.release()
        server_semaphore.acquire()
        map_file.seek(0)
        data = map_file.read(size)
        while data[-1] != 50:
            map_file.seek(0)
            data = map_file.read(size)
        # print(data[-2:-1])
        client_semaphore.release()
        msgs += 2

    map_file.close()
    print('Received {} messages in {} second(s).'.format(msgs, duration))


if __name__ == '__main__':
    client_run()
