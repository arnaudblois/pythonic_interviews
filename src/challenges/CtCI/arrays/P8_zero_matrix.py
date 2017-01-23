#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 1.8 from CtCI
Write an algorithm such that if an element in an M x N matrix is 0,
its entire row and column are set to 0.
"""

import numpy as np


def zero_matrix_no_numpy(matrix):
    """
    First solution relying only on pure Python
    Scans through the matrix once, storing in sets the indices where zeroes
    have been detected (sets automatically removes duplicates).
    A second loop then zeroes the rows and cols as appropriate.
    Algo is 0(M x N) which is the best possible since all elements have to be
    touched in the general case.
    """
    if matrix == []:
        return []

    zero_col_indices = set()
    zero_row_indices = set()

    M = len(matrix)
    N = len(matrix[0])

    # We scan the matrix to locate all zeros
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == 0:
                zero_col_indices.add(j)
                zero_row_indices.add(i)

    for i, row in enumerate(matrix):
        if i in zero_row_indices:
            matrix[i] = [0] * N
        else:
            for j in zero_col_indices:
                matrix[i][j] = 0
    return matrix


def zero_matrix_numpy(matrix):
    """
    2nd solution taking advantage of Numpy with its efficient "where" method and
    more advanced indexing
    """
    if matrix == []:
        return []
    matrix = np.matrix(matrix)
    a = np.where(matrix == 0)
    zero_row_indices = list(set(a[0]))
    zero_col_indices = list(set(a[1]))
    #We then set the rows and cols to zero
    matrix[::, zero_col_indices] = 0
    matrix[zero_row_indices, ::] = 0
    return matrix.tolist()
