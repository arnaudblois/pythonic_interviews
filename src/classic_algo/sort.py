#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the most common sorting algorithms
    - bubble sort
    - selection sort
    - insertion sort
    - shell sort
    - quicksort
    - merge sort
    - heapsort

For the record, Python sorted uses by default timsort which is a hybrid stable
sorting algorithm, running in O(n) for best case (list already sorted) to
O(n log n). It does so by taking advantage of the fact that real-life lists
often have some partial ordering.
"""


def bubble_sort(a):
    """
    In this algo, the i-th pass starts at the first element and compare
    sequencially each element to the next, swapping them if necessary, up to
    n-i. The biggest element 'bubbles up' to the n-i position. This runs in
    O(n^2): n-1 passes of O(n) comparisons.

    Note the use of the pythonic swap operation "a, b = b, a", not requiring the
    use of a temporary storage variable.
    """
    length = len(a)
    for pass_number in range(length):
        for i in range(1, length - pass_number):
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]
    return a


def short_bubble_sort(a):
    """
    Variant of the short bubble, taking advantage of the fact we know that if no
    value has been swaped, the list is sorted and we can return early.
    """
    length = len(a)
    for pass_number in range(length):
        has_swapped = False
        for i in range(1, length - pass_number):
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]
                has_swapped = True
        if not has_swapped:
            break
    return a


def selection_sort(a):
    """
    Swapping values can be an expensive operation. At the i-th pass, the
    selection sort finds the largest values and swap it with the value at n - i,
    performing faster than bubble sort. Note this can be shortened same as
    above (not shown here for clarity)
    """
    length = len(a)
    for pass_number in range(length):
        i_max, max_value = 0, a[0]
        for i in range(1, length - pass_number):
            if a[i] > max_value:
                i_max = i
                max_value = a[i]

        last_index = length - pass_number - 1
        a[i_max], a[last_index] = a[last_index], a[i_max]
    return a


def insertion_sort(a):
    """
    The insertion sort uses another strategy: at the i-th pass, the i first
    terms are sorted and it inserts the i + 1 term where it belongs by shifting
    right all elements greater one notch right to create a gap to insert it.
    It also runs in O(n^2)
    """
    length = len(a)
    for pass_number in range(1, length):
        value = a[pass_number]
        i = pass_number - 1
        while i > -1 and value < a[i]:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = value
    return a



def shell_sort(list_to_order):
    """
    """
    raise NotImplementedError



def merge(a, b):
    """
    helper function used by merge_sort
    combines two sorted lists into one sorted list
    """
    i, j = 0, 0
    sorted_list = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    sorted_list += a[i:]
    sorted_list += b[j:]
    return sorted_list


def merge_sort(a):
    """
    """
    if a == []:
        return []

    if len(a) == 1:
        return a
    midpoint = len(a)//2
    left = a[:midpoint]
    right = a[midpoint:]
    a = merge(merge_sort(left), merge_sort(right))
    return a


def quick_sort(list_to_order):
    """
    """
    raise NotImplementedError


def heap_sort(list_to_order):
    """
    """
    raise NotImplementedError
