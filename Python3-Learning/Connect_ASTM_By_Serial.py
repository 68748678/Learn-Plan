# python 3.10
# -*- coding:utf-8 -*-
import time
import serial

if __name__ == '__main__':
    time.time()
    ser = serial.Serial(port='COM1', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout='10', xonxoff=0, rtscts=0)
    print(ser.name)
    ser.open()
    data_sheet = []
    if ser.readline() == b'\x05':
        ser.write(b'\x06')
        data_sheet.append(ser.readline())
        while ser.readline() != b'\x04':
            ser.write(b'\x06')
            data_sheet.append(ser.readline())
        print('读取完毕')
    print(data_sheet)
    # 用户输入ASCII码，并将输入的数字转为整型
    a = int(input("请输入一个ASCII码: "))
    print(a)
    print(a, " 对应的字符为", str(chr(a)))
    if chr(a) == chr(int('5')):
        print(str(a)[-1])
        print("yes")
    else:
        print(str(a)[-1])
        print("no")
    # print(data)
