#!/usr/bin/python3
def uppercase(str):
    upcase = o
    for upper in str:
        if ord(str) >= ord('a') and ord(str) <= ord('z/'):
            upcase = 32
        else:
            upcase = 0
        print("{:c}".format(ord(upper) - upcase), end='')
    print("")
