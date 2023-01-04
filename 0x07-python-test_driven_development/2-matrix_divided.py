#!/usr/bin/python3
""" function that divides all ements of a matrix """


def matrix_divided(matrix, div):
    """ 
    matrix must be a list of lists of integers or floats
    each row of the matrix must be of the same size
    div must be a number 
    div can't be equal to zero 
    """
    new_matrix = []
    new_matrix1 = []
    if not matrix or type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        for num in elements:
            if not type(num) in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if len(elements) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for elements in range(len(matrix)):
        new_matrix = []
        for num in range(len(matrix[elements])):
            new_matrix.append(round(matrix[elements][num] / div, 2))
        new_matrix1.append(new_matrix)
    return new_matrix1 
