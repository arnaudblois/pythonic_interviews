from ..P3_urlify import urlify
from urllib.parse import quote_plus

test_list = [('Remove the spaces', 'Remove+the+spaces'), ]


def test_urlify():
    for test_string in test_list:
        assert urlify(test_string[0]) == test_string[1]
        assert quote_plus(test_string[0]) == urlify(test_string[0])
