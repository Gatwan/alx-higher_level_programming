#!/usr/bin/python3
for alPH in reversed(range(97, 123)):
    print("{}".format(chr(alPH) if alPH % 2 == 0 else chr(alPH - 32)), end='')
