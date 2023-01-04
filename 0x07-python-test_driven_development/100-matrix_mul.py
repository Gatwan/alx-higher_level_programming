#!/usr/bin/python3
""" function that multiplies 2 matrices """


def matrix_mul(m_a, m_b):
    """ m_a and m_b must be an list of lists of integers or floats
        """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(elmnt, (int, float)) for row in m_a for elmnt in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(elmnt, (int, float)) for row in m_b for elmnt in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0] != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize result matrix
    rows = len(m_a)
    col = len(m_b[0])

    mat = [[0 for _ in range(col)] for _ in range(rows)]

    # iterate rows of m_a
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                mat[i][j] += m_a[i][k] * m_b[k][j]
    return mat
