from ..P8_zero_matrix import zero_matrix_no_numpy, zero_matrix_numpy
from copy import deepcopy


def test_empty():
    assert zero_matrix_no_numpy([]) == []
    assert zero_matrix_numpy([]) == []


def test_single_row_no_zero():
    matrix = [[1, 3, 2, 4]]
    zeroed = [[1, 3, 2, 4]]
    assert zero_matrix_no_numpy(deepcopy(matrix)) == zeroed
    assert zero_matrix_numpy(deepcopy(matrix)) == zeroed


def test_single_row_with_zero():
    matrix = [[1, 3, 2, 1, 3, 0]]
    zeroed = [[0, 0, 0, 0, 0, 0]]
    assert zero_matrix_no_numpy(deepcopy(matrix)) == zeroed
    assert zero_matrix_numpy(deepcopy(matrix)) == zeroed


def test_single_col_with_zero():
    assert zero_matrix_no_numpy([[1], [3], [2], [4]]) == [[1], [3], [2], [4]]
    assert zero_matrix_numpy([[1], [3], [2], [4]]) == [[1], [3], [2], [4]]


def test_6x2_matrix():
    matrix = [
        [5, 1, 6, 2, 0],
        [1, 2, 3, 4, 5],
    ]

    zeroed = [
        [0, 0, 0, 0, 0],
        [1, 2, 3, 4, 0],
    ]
    assert zero_matrix_no_numpy(deepcopy(matrix)) == zeroed
    assert zero_matrix_numpy(deepcopy(matrix)) == zeroed


def test_6x5_matrix():
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 0, 8, 9, 8],
        [7, 6, 5, 4, 3],
        [2, 1, 2, 3, 4],
        [5, 0, 7, 0, 9],
        [8, 7, 6, 5, 4],
    ]

    zeroed = [
        [1, 0, 3, 0, 5],
        [0, 0, 0, 0, 0],
        [7, 0, 5, 0, 3],
        [2, 0, 2, 0, 4],
        [0, 0, 0, 0, 0],
        [8, 0, 6, 0, 4],
    ]
    assert zero_matrix_no_numpy(deepcopy(matrix)) == zeroed
    assert zero_matrix_numpy(deepcopy(matrix)) == zeroed
