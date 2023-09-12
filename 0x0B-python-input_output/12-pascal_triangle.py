#!/usr/bin/python3
"""Contains the function pascal_triangle"""


def pascal_triangle(n):
    """Returns a list of integers representing Pascal's triangle"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tria = triangles[-1]
        tmp = [1]
        for i in range(len(tria) - 1):
            tmp.append(tria[i] + tria[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
