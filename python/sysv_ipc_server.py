import sysv_ipc
import time


def server_run():
    memory_size = sysv_ipc.PAGE_SIZE * (1 << 9)
    mem = sysv_ipc.SharedMemory(1, sysv_ipc.IPC_CREX, size=memory_size)
    server_semaphore = sysv_ipc.Semaphore(2, sysv_ipc.IPC_CREX)
    client_semaphore = sysv_ipc.Semaphore(3, sysv_ipc.IPC_CREX)
    size = 1 << 20
    data1 = b'a' * size
    data2 = b'b' * size
    duration = 1
    # end = time.time() + duration
    # msgs = 0

    while True:
        mem.write(data1)
        server_semaphore.release()
        client_semaphore.acquire()
        mem.write(data2)
        server_semaphore.release()
        client_semaphore.acquire()
    # mem.detach()
    # mem.remove()


def remove_run():
    mem = sysv_ipc.SharedMemory(1)
    mem.detach()
    mem.remove()
    server_semaphore = sysv_ipc.Semaphore(2)
    server_semaphore.remove()
    client_semaphore = sysv_ipc.Semaphore(3)
    client_semaphore.remove()


if __name__ == '__main__':
    # server_run()
    remove_run()
