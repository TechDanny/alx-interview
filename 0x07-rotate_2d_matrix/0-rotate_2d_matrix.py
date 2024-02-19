#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotates matrix 2D 90 degrees clockwise
    """
    "matrix transponse"
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    "reverse from matrix transponse"
    x = len(matrix)
    for i in range(x//2):
        for j in range(x):
            matrix[j][i], matrix[j][x-1-i] = matrix[j][x-1-i], matrix[j][i]

    return matrix
