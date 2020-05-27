import mmap
import time


def client_run():
    f = open('/tmp/mmap', 'r+b')
    mm = mmap.mmap(f.fileno(), 0)
    cache_line_size = 64
    base_address = 0
    write_finish = base_address + cache_line_size
    read_finish = write_finish + cache_line_size
    data_address = read_finish + cache_line_size
    size = 1 << 20
    duration = 1
    end = time.time() + duration
    msgs = 0
    while time.time() < end:
        mm.seek(write_finish)
        while mm.read_byte() != 1:
            mm.seek(write_finish)
        mm.seek(write_finish)
        mm.write(b'0')
        mm.seek(data_address)
        data = mm.read(size)
        mm.seek(read_finish)
        mm.write(b'1')
        msgs += 1

    mm.close()
    print('Received {} messages in {} second(s).'.format(msgs, duration))


if __name__ == '__main__':
    client_run()
