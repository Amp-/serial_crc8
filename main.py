import serial
import uart
import crc8
import test
method = 'com'
port = '/dev/ttyUSB0'
baudrate = '115200'

def serail_data(com:uart.Serial):
    with serial.Serial() as ser:
        ser.port = com.port
        ser.baudrate = com.baudrate
        ser.open()
        return ser.read()

def read_data(data):
    t = data.hex()
    return t

def parse_data():
    hash = crc8.crc8()
    hash.update(b'123')
    print(hash.hexdigest())


if __name__ == '__main__':
    # com = uart.Serial(port=port,baudrate=baudrate)
    # data = serail_data()
    # read_data(data)
    parse_data()
