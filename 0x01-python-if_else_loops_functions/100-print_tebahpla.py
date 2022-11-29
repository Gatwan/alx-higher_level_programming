#!/usr/bin/python3
for letter in reversed(range(97, 123)):
    print("{}".format(chr(letter) if letter % 2 == 0 else chr(letter - 32)), end='')
