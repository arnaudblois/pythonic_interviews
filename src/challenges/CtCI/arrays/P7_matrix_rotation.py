#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 1.7 from CtCI
rotate a matrix by 90° in the anticlockwise direction
Note that this is already implemented in Numpy Rot90
"""

from math import ceil
from pprint import pprint


def rotate_90(matrix):
    """
    rotates the matrix by 90° in the anticlockwise direction. Does it layer by
    layer, working its way towards the center. The indexing is fairly tricky,
    it is advised to draw it to understand what is happening.
    performs the transformation in place, runs in O(n^2)
    """
    N = len(matrix)
    for i in range(ceil(N/2)):
            lim = N - i - 1
            for step in range(N - 2 * i - 1):
                current_value = matrix[i][i + step]
                matrix[i][i + step] = matrix[i + step][lim]
                matrix[i + step][lim] = matrix[lim][lim - step]
                matrix[lim][lim - step] = matrix[lim - step][i]
                matrix[lim - step][i] = current_value
    return matrix
