#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)

    elem = len(my_list)
    if idx > elem - 1:
        return (my_list)

    original_list = my_list.copy()
    original_list[idx] = element

    return (original_list)
