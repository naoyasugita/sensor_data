import smbus
import time

channel = 1
address = 0x68
bus = smbus.SMBus(channel)

bus.write_i2c_block_data(address, 0x6B, [0x80])
time.sleep(0.1)

bus.write_i2c_block_data(address, 0x6B, [0x00])
time.sleep(0.1)

while True:
    data = bus.read_i2c_block_data(address, 0x3B ,6)
    x = (2.0 / float(0x8000)) * (data[0] << 8 | data[1])
    y = (2.0 / float(0x8000)) * (data[2] << 8 | data[3])
    z = (2.0 / float(0x8000)) * (data[4] << 8 | data[5])
    print ("X:%+8.7f" % x)
    print ("Y:%+8.7f" % y)
    print ("Z:%+8.7f" % z)
    time.sleep(1)

