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
def write_date(com:uart.Serial):
    with serial.Serial() as ser:
        ser.port = com.port
        ser.baudrate = com.baudrate
        ser.open()
        crc = parse_data(b'0x00')
        buffer = b'[0xAA,0x01,0x00,0xf6]'
        ser.write(buffer)

def parse_data(data):
    hash = crc8.crc8()
    hash.update(data)
    return hash.hexdigest()


if __name__ == '__main__':
    com = uart.Serial(port=port,baudrate=baudrate)
    data = serail_data(com)
    write_date(com)
    while True:

        t = read_data(data)
        print(t)

    parse_data(t)
