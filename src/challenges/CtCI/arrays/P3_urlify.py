#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Problem 1.3 -- CtCI
Replace the spaces of a string by "+" as per the url encoding.
Note that in real life proper url encoding is a bit trickier as all characters
have to be ASCII encoded, this is normally done with quote_plus in urllib.parse
"""

from collections import Counter

def urlify(string):
    """
    replace spaces with '+'
    """
    string = string.strip()
    return string.replace(' ', '+')
