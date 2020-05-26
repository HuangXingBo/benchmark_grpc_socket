import sysv_ipc
import time


def client_run():
    mem = sysv_ipc.SharedMemory(1)
    server_semaphore = sysv_ipc.Semaphore(2)
    client_semaphore = sysv_ipc.Semaphore(3)
    size = 1 << 20
    duration = 10
    end = time.time() + duration
    msgs = 0
    while time.time() < end:
        server_semaphore.acquire()
        data = mem.read(size)
        client_semaphore.release()
        msgs += 1
    mem.detach()
    print('Received {} messages in {} second(s).'.format(msgs, duration))


if __name__ == '__main__':
    client_run()
