#!/usr/bin/env python

import struct
import time

import broadlink
import fire

class Error(Exception):
    pass

def main(device_index=0):
    'Entry point'
    devices = broadlink.discover(timeout=5)
    if devices == []:
        raise Error('Cannot find any device')
    device = devices[device_index]
    device.auth()
    device.enter_learning()
    print('Waiting for IR input...')
    while True:
        ir_packet = device.check_data()
        if ir_packet:
            print('Received IR packet is:')
            print(ir_packet)
            print('As uchar array:')
            uchar_array = struct.unpack('<' + 'B' * len(ir_packet), ir_packet)
            print('[{}]'.format(', '.join([str(uchar) for uchar in uchar_array])))
            break
        time.sleep(1)


if __name__ == '__main__':
    fire.Fire(main)
