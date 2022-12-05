#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxnum = my_list[0]

        for a in my_list:
            if a > maxnum:
                maxnum = a
        return (maxnum)
