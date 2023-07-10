import serial
import uart

import test
method = 'com'
port = '/dev/ttyUSB0'
baudrate = '115200'

def serail_data(com:uart.Serial):
    with serial.Serial() as ser:
        ser.port = com.port
        ser.baudrate = com.baudrate
        ser.open()
        return ser.read(4)

def read_data(data):
    t = data.hex(' ')
    g = t.split()
    # return t
    print(type(data))
    print(data[0:1]+data[1:2])
    return data
def write_date(com:uart.Serial):
    with serial.Serial() as ser:
        ser.port = com.port
        ser.baudrate = com.baudrate
        ser.open()
        buffer = b'[AA,02,00,00]'
        ser.write(buffer)

if __name__ == '__main__':
    com = uart.Serial(port=port,baudrate=baudrate)
    data = serail_data(com)
    # write_date(com)
    t = read_data(data)
    # print(data[3:4])
    # print(data[-1:-1])
    print(t)



