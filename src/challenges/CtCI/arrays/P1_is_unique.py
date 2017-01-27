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
    using Counter is the most Pythonic way to do so -- if all characters are
    unique, no count should be above 0
    """
    c = Counter(string.lower())
    return not any(letter_count > 1 for letter_count in c.values())


def is_unique_no_extra_space(string):
    """
    added constraint to use O(1) space. In this follow-up case, we can't build
    a Counter object (O(n) space) and have to enumerate the string once,
    checking every time that the current letter does not appear in the portion
    of the string following it (no need to check over the whole string at
    every iteration.)
    """
    for i, ref_letter in enumerate(string):
        for letter in string[i + 1:]:
            if letter == ref_letter:
                return False
    return True
