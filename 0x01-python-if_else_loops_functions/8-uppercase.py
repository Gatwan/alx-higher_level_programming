#!/usr/bin/python3
def uppercase(str):
    upcase = 0
    for upper in str:
        if ord(upper) >= ord('a') and ord(upper) <= ord('z'):
            upcase = 32
        else:
            upcase = 0
        print("{:c}".format(ord(upper) - upcase), end='')
    print("")
