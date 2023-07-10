import serial
import uart
import crc_maxim
import test
method = 'com'
port = '/dev/ttyUSB0'
baudrate = '115200'
parity = 'PARITY_EVEN'


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
    while True:
        write_2()
        # read_data_2()


