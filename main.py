import serial
import uart
import threading
import crc_maxim
import test
method = 'com'
port = '/dev/ttyUSB0'
baudrate = '115200'

in_list = []
out_flag = 0
ser = serial.Serial(port,baudrate,timeout=1)

def serail_data(com:uart.Serial):
    with serial.Serial() as ser:
        ser.port = com.port
        ser.baudrate = com.baudrate
        ser.parity = com.parity
        ser.open()
        return ser.read(4)

def read_data(data):
    t = data.hex(' ')
    g = t.split()
    # print(hex(crc_maxim.DallasMaximCRC8(data[1:2]+data[2:3])))
    return data

def write_2():
    with serial.Serial() as ser:
        ser.baudrate = baudrate
        ser.port = port
        ser.open()
        ser.write(b'\xaa\x01\x00\xc4')
        t = ser.read(4)
        print(t[1:2])

def fn_in():
    global in_list
    while True:
        in_len = 0
        while in_len < 1:
            in_st = ser.read(4)
            in_len = len(in_st)
        in_list.append(in_st)
        print(in_st)

def fn_out():
    global out_flag
    out_flag = 1
def fn_send():
    ser.write(b'\xaa\x01\x00\xc4')
def read_data_2():
    ser = serial.Serial(port, baudrate, timeout=1)
    t = ser.read(4)
    print(t)
def write_date(com:uart.Serial):
    with serial.Serial() as ser:
        ser.port = com.port
        ser.baudrate = com.baudrate
        ser.parity = com.parity
        ser.open()
        # buffer = b'\xaa\x04\x00\3\b'
        buffer = b'\xaa\x01\x00\xc4'
        ser.write(buffer)

if __name__ == '__main__':
    # com = uart.Serial(port=port,baudrate=baudrate,parity=parity)
    # data = serail_data(com)
    # write_date(com)
    # t = read_data(data)
    # print(t)
    # while True:
    #     write_2()
        # read_data_2()
    while True:
        t = input(': ')
        fn_send()
        tr_in = threading.Thread(target = fn_in())
        tr_in.daemon = True
        tr_in.start()




