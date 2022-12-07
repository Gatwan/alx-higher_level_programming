#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for r in matrix:
        sq_r = []
        for num in r:
            sq_num = num * num
            sq_r.append(sq_num)
        sq_matrix.append(sq_r)
    return sq_matrix
