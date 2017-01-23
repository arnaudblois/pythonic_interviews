from ..P1_is_unique import is_unique, is_unique_no_extra_space

def test_empty():
    """
    test for empty input -- returns True by convention
    """
    assert is_unique('') == True
    assert is_unique_no_extra_space('') == True

def test_single():
    """
    test for a single letter -- returns True
    """
    assert is_unique('a') == True
    assert is_unique_no_extra_space('a') == True

def test_negative():
    """
    test for a string with two non-unique characters -- returns False
    """
    string = 'abcdefghai'
    assert is_unique(string) == False
    assert is_unique_no_extra_space(string) == False

def test_positive():
    """
    test for a long string of unique characters -- returns True
    """
    string = 'abcdefghijklmnopqrstuvwxyz'
    assert is_unique(string) == True
    assert is_unique_no_extra_space(string) == True
