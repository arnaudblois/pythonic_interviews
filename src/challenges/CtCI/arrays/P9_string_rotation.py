"""
    Given two strings, check if s2 is a rotation of sl using only one
    call to the built-in "in"

    >>> is_rotated_string("ttleponymyli", "mylittlepony")
    True
"""


def is_rotated_string_naive(s1, s2):
    """
    A very naive implementation of the function, performing all the possible
    rotations and comparing until both strings match
    Runtime is O(n^2) as we expect O(n) comparisons of O(n) characters
    it doesn't use the "in" function!!
    """
    s1, s2 = s1.lower(), s2.lower()
    length = len(s1)
    if s1 == '' and s2 == '':
        return True  #  Convention: '' in '' evaluates to True
    if not len(s2) == length:
        return False
    is_rotated = False
    for shift in range(length):
        print("comparing", s1, s2[shift:] + s2[:shift])
        is_rotated |= s1 == s2[shift:] + s2[:shift]
    return is_rotated


def is_rotated_string(s1, s2):
    """
    The pythonic solution is found by considering the clue: use "in" only once.
    Assuming the string is rotated, it can be thought as being split in this way
    s1 = part1 + part2 and s2 = part2 + part1. We can notice that s2 + s2 =
    part2 + part1 + part2 + part1 = part2 + s1 + part1
    -> s1 in s2 + s2 is the answer we need, this comparison is done is O(n)
    """
    s1, s2 = s1.lower(), s2.lower()
    if not len(s2) == len(s1):
        return False
    return s1 in s2 + s2
