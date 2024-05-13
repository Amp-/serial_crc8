import serial
import uart
import threading
import time
import crc_maxim
import test
method = 'com'
port = '/dev/ttyUSB0'
#port = 'COM8'
baudrate = '115200'
start_byte = b'\xaa'
in_list = []
out_flag = 0
ser = serial.Serial(port,baudrate,timeout=1)

def read_data(data):
    t = data.hex(' ')
    g = t.split()
    # print(hex(crc_maxim.DallasMaximCRC8(data[1:2]+data[2:3])))
    return data
def fn_in():
    global in_list
    while True:
        in_len = 0
        while in_len < 1:
            in_st = ser.read(4)
            in_len = len(in_st)
            if len(in_st) > 0:
                if chek_data(in_st):
                    in_list.append(in_st)
                    time.sleep(1)

def chek_data(data):
    b_opt_and_data = data[1:3]
    crc = bytes.fromhex(crc_maxim.DallasMaximCRC8(b_opt_and_data))
    if data.startswith(start_byte) and data.endswith(crc):
        return True

def fn_out():
    global out_flag
    out_flag = 1
def fn_send(op_code, data):
    s_byte = start_byte
    o_code = bytes.fromhex(op_code)#04
    d_byte = bytes.fromhex(data)#00
    crc = bytes.fromhex(crc_maxim.DallasMaximCRC8(o_code+d_byte))
    print(crc)
    send_byte = s_byte+o_code+d_byte+crc
    ser.write(send_byte)

def fn_send_2(op_code, data):
    s_byte = start_byte
    crc = bytes.fromhex(crc_maxim.DallasMaximCRC8(op_code+data))
    send_byte = s_byte + op_code + data+crc
    # print(send_byte)
    ser.write(send_byte)

if __name__ == '__main__':
    tr_out = threading.Thread(target=fn_in)
    tr_out.daemon = True
    tr_out.start()
    while True:
        t = input(': ')
        if t == '1':
            fn_send(op_code='04', data='00')
            # fn_send_2(op_code=b'\x04', data=b'\x00')
            # fn_send(op_code='04', data='00')
            if len(in_list) >0:
                g = in_list.pop(0)
                print(g)
        if t == '2':
            fn_send(op_code='01', data='00')
            if len(in_list) > 0:
                g = in_list.pop(0)
                print(g)
        if t == '3':
            fn_send(op_code='05', data='00')
            fn_send(op_code='07', data='00')
            if len(in_list) > 0:
                g = in_list.pop(0)
                print(g)
        if t == '4':
            fn_send(op_code='05', data='FF')
            fn_send(op_code='07', data='FF')
            if len(in_list) > 0:
                g = in_list.pop(0)
                print(g)
        if t == '5':
            fn_send(op_code='02', data='80')
            if len(in_list) > 0:
                g = in_list.pop(0)
                print(g)

    # write_2()




