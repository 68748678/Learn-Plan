# python 3.10
# -*- coding:utf-8 -*-
import time
import serial

if __name__ == '__main__':
    time.time()
    # ser = serial.serial_for_url(url='socket://192.168.1.200:502', baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
    ser = serial.serial_for_url(url='COM2', baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
    print(ser.name)
    data_sheet = []
    val = ser.read(1)
    if val == b'\x05':
        while True:
            ser.write(b'\x06')
            if ser.read(1) ==b'\x04':
                break
            res = ser.readline()
            data_sheet.append(res)
        print('读取完毕')
        print(data_sheet)
