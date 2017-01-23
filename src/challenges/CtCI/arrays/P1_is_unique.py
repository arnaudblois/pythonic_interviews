#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 1 from CtCI
determines if all characters in a string are unique
"""

import structures
from collections import Counter


def is_unique(string):
    """
    using Counter is the most Pythonic way to do so -- no count should be above
    0
    """
    c = Counter(string.lower())
    return not any(letter_count > 1 for letter_count in c.values())


def is_unique_no_extra_space(string):
    """
    added constraint to use O(1) space.
    """
    for i, ref_letter in enumerate(string):
        for letter in string[i + 1:]:
            if letter == ref_letter:
                return False
    return True
