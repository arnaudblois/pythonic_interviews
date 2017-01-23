from ..P9_string_rotation import is_rotated_string, is_rotated_string_naive


def test_rotate_empty():
    """ '' in '' == True by convention """
    s1, s2 = '', ''
    assert is_rotated_string_naive(s1, s2) == True
    assert is_rotated_string(s1, s2) == True


def test_rotate_one_element_true():
    s1, s2 = 'a', 'a'
    assert is_rotated_string_naive(s1, s2) == True
    assert is_rotated_string(s1, s2) == True


def test_rotate_one_element_false():
    s1, s2 = 'a' , 'b'
    assert is_rotated_string_naive(s1, s2) == False
    assert is_rotated_string(s1, s2) == False


def test_same_string():
    s1, s2 = 'abcdefgh', 'abcdefgh'
    assert is_rotated_string_naive(s1, s2) == True
    assert is_rotated_string(s1, s2) == True


def test_different_lengths():
    s1, s2 = 'abcde', 'abcdef'
    assert is_rotated_string_naive(s1, s2) == False
    assert is_rotated_string(s1, s2) == False


def test_repeated_pattern():
    s1, s2 = 'tictactic', 'tictictac'
    assert is_rotated_string_naive(s1, s2) == True
    assert is_rotated_string(s1, s2) == True


def test_rotated_string():
    s1, s2 = 'ttleponymyli', 'mylittlepony'
    assert is_rotated_string_naive(s1, s2) == True
    assert is_rotated_string(s1, s2) == True


def test_not_rotated_string():
    s1, s2 = 'Python', 'ythonC'
    assert is_rotated_string_naive(s1, s2) == False
    assert is_rotated_string(s1, s2) == False
