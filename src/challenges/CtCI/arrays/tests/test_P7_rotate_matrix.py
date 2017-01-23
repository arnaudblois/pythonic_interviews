from ..P7_matrix_rotation import rotate_90


def test_rotate_empty():
    matrix = []
    rotated_matrix = []
    assert rotate_90(matrix) == rotated_matrix


def test_rotate_one_element():
    matrix = [['a'], ]
    rotated_matrix = [['a'], ]
    assert rotate_90(matrix) == rotated_matrix


def test_rotate_N_2():
    matrix = [
        ['a', 'b'],
        ['c', 'd'],
    ]

    rotated_matrix = [
        ['b', 'd'],
        ['a', 'c'],
    ]
    assert rotate_90(matrix) == rotated_matrix


def test_rotate_N_3():
    matrix = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
    ]

    rotated_matrix = [
        ['c', 'f', 'i'],
        ['b', 'e', 'h'],
        ['a', 'd', 'g'],
    ]
    assert rotate_90(matrix) == rotated_matrix


def test_rotate_N_5():
    matrix = [
        ['a', 'b', 'c', 'd', 'e'],
        ['f', 'g', 'h', 'i', 'j'],
        ['k', 'l', 'm', 'n', 'o'],
        ['p', 'q', 'r', 's', 't'],
        ['u', 'v', 'w', 'x', 'y'],
    ]

    rotated_matrix = [
        ['e', 'j', 'o', 't', 'y'],
        ['d', 'i', 'n', 's', 'x'],
        ['c', 'h', 'm', 'r', 'w'],
        ['b', 'g', 'l', 'q', 'v'],
        ['a', 'f', 'k', 'p', 'u'],
    ]
    assert rotate_90(matrix) == rotated_matrix
