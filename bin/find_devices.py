#!/usr/bin/env python

import broadlink


def main():
    'Find broadlink devices on local network and print it'
    print('Looking for broadlink devices')
    devices = broadlink.discover(timeout=5)
    print('%d devices on your local network.' % (len(devices)))
    for device in devices:
        print('IP address -- %s' % (device.host[0]))


if __name__ == '__main__':
    main()