package com.alibaba;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class JavaIpServer {
    public static void main(String[] args) throws IOException {
        ServerSocket ss = new ServerSocket(5000);
        Socket s = ss.accept();
        System.out.println("start");
        InputStream inputStream = s.getInputStream();
        OutputStream outputStream = s.getOutputStream();
        int size = 1 << 20;
        byte[] data = new byte[size];
        int len = data.length;
        byte[] sendData = new byte[32];
        while (true) {
            int writen = 0;
            while (writen < len) {
                int read_len = inputStream.read(data, writen, len - writen);
                writen += read_len;
            }
            outputStream.write(sendData);
            outputStream.flush();
        }
    }
}
