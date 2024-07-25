#!/usr/bin/env python3
"""
method that determine if a given data set represents a calid UTF - 8
encoding
"""


def validUTF8(data):
    """
    this method check the data is UTF - 8 coding
    """
    n_bytes = 0
    # mask1 = 1 << 7
    # mask2 = 1 << 6

    for num in data:
        bitRep = format(num, '#010b')[-8:]

        if n_bytes == 0:
            for bit in bitRep:
                if bit == '0':
                    break
                n_bytes += 1

            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (bitRep[0] == '1' and bitRep[1] == '0'):
                return False
        n_bytes -= 1
    return n_bytes == 0
