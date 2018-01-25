from ..P9_string_rotation import is_rotated_string, is_rotated_string_naive


def test_rotate_empty():
    """ '' in '' is True by convention."""
    s1, s2 = '', ''
    assert is_rotated_string_naive(s1, s2)
    assert is_rotated_string(s1, s2)


def test_rotate_one_element_true():
    s1, s2 = 'a', 'a'
    assert is_rotated_string_naive(s1, s2)
    assert is_rotated_string(s1, s2)


def test_rotate_one_element_false():
    s1, s2 = 'a', 'b'
    assert not is_rotated_string_naive(s1, s2)
    assert is_rotated_string(s1, s2)


def test_same_string():
    s1, s2 = 'abcdefgh', 'abcdefgh'
    assert is_rotated_string_naive(s1, s2)
    assert is_rotated_string(s1, s2)


def test_different_lengths():
    s1, s2 = 'abcde', 'abcdef'
    assert not is_rotated_string_naive(s1, s2)
    assert not is_rotated_string(s1, s2)


def test_repeated_pattern():
    s1, s2 = 'tictactic', 'tictictac'
    assert is_rotated_string_naive(s1, s2)
    assert is_rotated_string(s1, s2)


def test_rotated_string():
    s1, s2 = 'ttleponymyli', 'mylittlepony'
    assert is_rotated_string_naive(s1, s2)
    assert is_rotated_string(s1, s2)


def test_not_rotated_string():
    s1, s2 = 'Python', 'ythonC'
    assert not is_rotated_string_naive(s1, s2)
    assert not is_rotated_string(s1, s2)
