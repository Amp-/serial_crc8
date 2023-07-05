import serial
import uart
import crc8
import test
method = 'com'
port = '/dev/ttyUSB0'
baudrate = '9600'

def serail_data(com:uart.Serial):
    with serial.Serial() as ser:
        ser.port = com.port
        ser.baudrate = com.baudrate
        ser.open()
        return ser.read()

def read_data(data):
    t = data.hex()
    return t

def parse_data(data):
    hash = crc8.crc8()
    hash.update(data.encode())
    print(hash.hexdigest())


if __name__ == '__main__':
    com = uart.Serial(port=port,baudrate=baudrate)

    while True:
        data = serail_data(com)
        t = read_data(data)
        # print(t)
        parse_data(t)
