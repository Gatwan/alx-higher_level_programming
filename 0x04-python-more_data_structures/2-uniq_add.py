#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_elements = set()
    for i in my_list:
        uniq_elements.add(i)
    sum = 0
    for i in uniq_elements:
        sum += i
    return sum
