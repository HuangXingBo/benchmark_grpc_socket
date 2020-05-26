# coding=utf-8
import os
import mmap
import time
import posix_ipc

size = os.statvfs('.')[1]

mem = posix_ipc.SharedMemory('/foo')
f = mmap.mmap(mem.fd, size, access=mmap.ACCESS_WRITE)
while True:
    print(f[:10])
    time.sleep(3)
