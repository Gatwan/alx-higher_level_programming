#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        num = []

        for a in my_list:
            if a % 2 == 0:
                num.append(True)
            else:
                num.append(False)
        return num
