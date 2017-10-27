import smbus
import time

#flg = False

arr = [[],[],[]]

channel = 1
address = 0x68
bus = smbus.SMBus(channel)

bus.write_i2c_block_data(address, 0x6B, [0x80])
time.sleep(0.1)

bus.write_i2c_block_data(address, 0x6B, [0x00])
time.sleep(0.1)

def main():
    try:
        while True:
            data = bus.read_i2c_block_data(address, 0x3B ,6)
            x = (2.0 / float(0x8000)) * (data[0] << 8 | data[1])
            y = (2.0 / float(0x8000)) * (data[2] << 8 | data[3])
            z = (2.0 / float(0x8000)) * (data[4] << 8 | data[5])

            arr[0].append(x)
            arr[1].append(y)
            arr[2].append(z)

            print ("X:%+8.7f" % x)
            print ("Y:%+8.7f" % y)
            print ("Z:%+8.7f" % z)
            # print(arr)
            time.sleep(1)
    except KeyboardInterrupt:
        return arr