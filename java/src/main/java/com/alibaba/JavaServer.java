package com.alibaba;

import org.jctools.util.PortableJvmInfo;
import sun.misc.Unsafe;

public class JavaServer {
    public static void main(String[] args) throws Exception {
        int size = 1 << 20;
        MMaper mmaper = new MMaper("/tmp/mmap", size * 10);
        long baseAddress = mmaper.getAddr();
        long writeFinish = baseAddress + PortableJvmInfo.CACHE_LINE_SIZE;
        long readFinish = writeFinish + PortableJvmInfo.CACHE_LINE_SIZE;
        long dataAddress = readFinish + PortableJvmInfo.CACHE_LINE_SIZE;
        byte[] data = new byte[size];
        for (int i = 0; i < data.length; i++) {
            data[i] = 'b';
        }
        Unsafe unsafe = SpscQueue.UNSAFE;
        int len = data.length;
        long start = System.currentTimeMillis();
        long duration = 10000;
        long end = start + duration;
        int msgs = 0;
        while (true) {
            unsafe.copyMemory(data, Unsafe.ARRAY_BYTE_BASE_OFFSET,
                    null, dataAddress, len);

            unsafe.putBoolean(null, writeFinish, true);
            boolean v = unsafe.getBooleanVolatile(null, readFinish);
            while (!v) {
                v = unsafe.getBooleanVolatile(null, readFinish);
            }
            unsafe.putBoolean(null, readFinish, false);
            msgs += 1;
        }
//        unsafe.copyMemory(null, address, res,
//                Unsafe.ARRAY_BYTE_BASE_OFFSET, len);
//        System.out.println(res[0]);
//        System.out.println(msgs);
//        mmaper.close();
    }
}
