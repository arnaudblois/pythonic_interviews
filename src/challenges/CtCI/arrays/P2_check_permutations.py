#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Problem 1.2 from CtCI
Check if a string is the permutation of another
"""
from unittest import TestCase
from collections import Counter


def check_permutation(string1, string2):
    """
    this is equivalent to have the same number of letters in both strings
    -> doable Pythonically with a one liner
    """
    return Counter(string1) == Counter(string2)
