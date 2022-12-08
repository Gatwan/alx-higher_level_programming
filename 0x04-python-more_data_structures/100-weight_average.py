#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    new = []
    div = []
    for i in range(len(my_list)):
        new.append(my_list[i][0] * my_list[i][1])
        div.append(my_list[i][1])

    return sum(new) / sum(div)
