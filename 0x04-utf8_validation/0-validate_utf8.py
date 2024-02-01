#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    This method that determines if a given data set
    represents a valid UTF-8 encoding
    """
    num_of_bytes = 0

    for x in data:
        if num_of_bytes == 0:
            if (x >> 7) == 0b0:
                continue
            elif (x >> 5) == 0b110:
                num_of_bytes = 1
            elif (x >> 4) == 0b1110:
                num_of_bytes = 2
            elif (x >> 3) == 0b11110:
                num_of_bytes = 3
            else:
                return False
        else:
            if (x >> 6) != 0b10:
                return False
            num_of_bytes -= 1

    return num_of_bytes == 0
