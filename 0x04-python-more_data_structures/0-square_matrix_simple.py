#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix"""
    new = []
    for rows in matrix:
        answer = list(map(lambda x: x**2, rows))
        new.append(answer)
    return new
