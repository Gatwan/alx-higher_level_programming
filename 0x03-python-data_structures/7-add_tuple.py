#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple1 = list(tuple_a)
    tuple2 = list(tuple_b)

    if len(tuple1) < 2:
        if tuple1 == 1:
            tuple1.append(0)
        else:
            tuple1.append(0)
            tuple1.append(0)

    if len(tuple2) < 2:
        if tuple2 == 1:
            tuple2.append(0)
        else:
            tuple2.append(0)
            tuple2.append(0)

    return (tuple1[0] + tuple2[0]), (tuple1[1] + tuple2[1])
