import posix_ipc
import mmap
import os
import time


def server_run():
    memory = posix_ipc.SharedMemory("pyflink", posix_ipc.O_CREAT, size=(1 << 20) * 10)
    server_semaphore = posix_ipc.Semaphore("server", posix_ipc.O_CREAT)
    client_semaphore = posix_ipc.Semaphore("client", posix_ipc.O_CREAT)
    map_file = mmap.mmap(memory.fd, memory.size)
    os.close(memory.fd)
    size = 1 << 20
    data1 = b'b' * size
    data2 = b'c' * size
    msgs = 0

    while True:
        map_file.seek(0)
        # print('first start')
        map_file.write(data1)
        map_file.write(b'1')
        # print('first end')
        server_semaphore.release()
        # print("server_semaphore first release")
        client_semaphore.acquire()
        # print('second start')
        map_file.seek(0)
        map_file.write(data2)
        map_file.write(b'2')
        # print('second end')
        server_semaphore.release()
        # print("server_semaphore second release")
        client_semaphore.acquire()
        msgs += 2
    map_file.close()
    memory.close_fd()
    memory.unlink()


def server_remove():
    memory = posix_ipc.SharedMemory("pyflink")
    memory.close_fd()
    memory.unlink()
    server_semaphore = posix_ipc.Semaphore("server")
    server_semaphore.close()
    server_semaphore.unlink()
    client_semaphore = posix_ipc.Semaphore("client")
    client_semaphore.close()
    client_semaphore.unlink()


if __name__ == '__main__':
    # server_run()
    server_remove()
