#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list:
        length = 0

        try:
            for i in range(0, x):
                print("{}".format(my_list[i]), end="")
                length += 1
            print()
            return length
        except IndexError:
            print()
            return length
    else:
        print()
        return 0
