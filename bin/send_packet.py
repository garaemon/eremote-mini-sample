#!/usr/bin/env python

import struct

import broadlink
import fire

class Error(Exception):
    pass

def main(device_index=0, *packet):
    'Entry point'
    devices = broadlink.discover(timeout=5)
    if devices == []:
        raise Error('Cannot find any device')
    device = devices[device_index]
    device.auth()
    ir_packet = struct.pack('<' + 'B'*len(packet), *packet)
    device.send_data(ir_packet)

if __name__ == '__main__':
    fire.Fire(main)

# ./bin/send_packet.py 0 38 0 88 0 0 1 39 149 16 21 17 19 19 55 19 18 17 20 18 19 17 20 17 19 19 55 18 56 18 19 19 54 19 55 18 56 18 56 17 56 17 20 18 19 19 18 17 57 17 19 19 18 18 20 17 19 19 55 18 56 20 54 18 18 19 55 19 55 18 56 17 56 17 0 5 38 0 1 38 76 17 0 12 91 0 1 39 76 17 0 13 5