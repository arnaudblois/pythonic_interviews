from ..P1_is_unique import is_unique, is_unique_no_extra_space


def test_empty():
    """Test for empty input -- returns True by convention."""
    assert is_unique('')
    assert is_unique_no_extra_space('')


def test_single():
    """Test for a single letter -- returns True"""
    assert is_unique('a')
    assert is_unique_no_extra_space('a')


def test_negative():
    """Test for a string with two non-unique characters -- returns False."""
    string = 'abcdefghai'
    assert not is_unique(string)
    assert not is_unique_no_extra_space(string)


def test_positive():
    """Test for a long string of unique characters -- returns True."""
    string = 'abcdefghijklmnopqrstuvwxyz'
    assert is_unique(string)
    assert is_unique_no_extra_space(string)
