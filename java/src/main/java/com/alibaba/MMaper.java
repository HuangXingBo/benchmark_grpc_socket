package com.alibaba;

import sun.nio.ch.FileChannelImpl;

import java.io.RandomAccessFile;
import java.lang.reflect.Method;
import java.nio.channels.FileChannel;

public class MMaper {
    private static final Method mmap;
    private static final Method unmmap;

    private long addr;
    private final long size;
    private final String loc;

    static {
        try {
            mmap = getMethod(FileChannelImpl.class, "map0", int.class, long.class, long.class);
            unmmap = getMethod(FileChannelImpl.class, "unmap0", long.class, long.class);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public MMaper(final String loc, long len) throws Exception {
        this.loc = loc;
        this.size = roundTo4096(len);
        map();
    }

    public long getSize() {
        return size;
    }

    public long getAddr() {
        return addr;
    }

    public void close() throws Exception {
        unmmap();
    }


    private static Method getMethod(Class<?> cls, String name, Class<?>... params) throws Exception {
        Method m = cls.getDeclaredMethod(name, params);
        m.setAccessible(true);
        return m;
    }

    private static long roundTo4096(long i) {
        return (i + 0xfffL) & ~0xfffL;
    }

    //Given that the location and size have been set, map that location
    //for the given length and set this.addr to the returned offset
    private void map() throws Exception {
        final RandomAccessFile backingFile = new RandomAccessFile(this.loc, "rw");
        backingFile.setLength(this.size);

        final FileChannel ch = backingFile.getChannel();
        this.addr = (long) mmap.invoke(ch, 1, 0L, this.size);

        ch.close();
        backingFile.close();
    }

    private void unmmap() throws Exception {
        if (addr != 0) {
            unmmap.invoke(null, addr, this.size);
        }
        addr = 0;
    }


}
