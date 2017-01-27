#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Problem 1.4 -- CtCI
checks if a string is the permutation of a palindrom
"""

from collections import Counter


def palindrome_permutation(string):
    """
    All palindromes follow the same rule, they have at most one letter whose
    count is odd, this letter being the "pivot" of the palindrome. The letters
    with an even count can always be permuted to match each other across the
    pivot.
    """
    string = string.strip().lower()
    c = Counter(string)
    l = [1 for letter_count in c.values() if letter_count % 2 == 1]
    return sum(l) < 2
