#!/usr/bin/python3
def no_c(my_string):
    without_c = ""

    for noc in my_string:
        if noc != "c" and noc != "C":
            without_c += noc
    return (without_c)
