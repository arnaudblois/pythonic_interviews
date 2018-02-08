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

For the record, Python built-in `sorted` uses by default timsort which
is a hybrid stable sorting algorithm, running in O(n) for best case
(list already sorted) to O(n log n). It does so by taking advantage of
the fact that real-life lists often have some partial ordering.
"""


def bubble_sort(a):
    """
    In this algo, the i-th pass starts at the first element and compare
    sequencially each element to the next, swapping them if necessary, up to
    n-i. The biggest element 'bubbles up' to the n-i position. This runs in
    O(n^2): n-1 passes of O(n) comparisons.

    Note the use of the pythonic swap operation "a, b = b, a", not requiring
    the use of a temporary storage variable.
    """
    length = len(a)
    for pass_number in range(length):
        for i in range(1, length - pass_number):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
    return a


def short_bubble_sort(a):
    """
    Variant of the short bubble, taking advantage of the fact we know that if
    no value has been swapped, the list is sorted and we can return early.
    """
    length = len(a)
    for pass_number in range(length):
        has_swapped = False
        for i in range(1, length - pass_number):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                has_swapped = True
        if not has_swapped:
            break
    return a


def selection_sort(a):
    """
    Swapping values can be an expensive operation. At the i-th pass, the
    selection sort finds the largest value and swap it with the value at n - i
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
    # at this point, we have reached the end of one of the lists, we therefore
    # append the remaining elements directly to sorted_list
    sorted_list += a[i:]
    sorted_list += b[j:]

    return sorted_list


def merge_sort(a):
    """
    Based on the divide and conquer approach, this algorithm runs in
    O(n log n).
    The array is split by the middle and each half is recursively
    sorted using merge_sort. The two sorted halves are then efficiently
    merged using the helper function above.
    """
    if len(a) <= 1:
        return a
    midpoint = len(a) // 2
    left = a[:midpoint]
    right = a[midpoint:]
    a = merge(merge_sort(left), merge_sort(right))
    return a


def quick_sort(a):
    """
    Another divide and conquer algorithm, quick sort relies on choosing a pivot
    value. The list is then partitioned using the scheme described in
    partition_helper. This placed the
    pivot in its correct position in the sorted list, the function is then
    called on the sublist a[:right_mark - 1] and a[right_mark+1:]
    """
    if len(a) <= 1:
        return a
    quicksort_helper(a, 0, len(a) - 1)
    return a


def quicksort_helper(a, first, last):
    """
    Helper function splitting the list at the pivot and recursively calling
    itself on the left and right parts of this splitpoint.
    """
    if first < last:
        split_point = partition_helper(a, first, last)
        quicksort_helper(a, first, split_point - 1)
        quicksort_helper(a, split_point + 1, last)


def partition_helper(a, first, last):
    """
    A left_mark index are initiated at the leftmost index available (ie
    not the pivot) and a right_mark at the rightmost. The left_mark is shifted
    right as long as a[left_mark] < pivot and the right_mark left as long as
    a[right_mark] > pivot. If left_mark < right_mark, the values at which the
    marks are stopped are swapped and the process continues until they cross.
    At this point, a[right_mark] and the pivot are swapped and the index of the
    right_mark is returned.
    """
    pivot_value = a[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while right_mark >= left_mark and a[left_mark] <= pivot_value:
            left_mark += 1

        while right_mark >= left_mark and a[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            a[left_mark], a[right_mark] = a[right_mark], a[left_mark]

    a[first], a[right_mark] = a[right_mark], a[first]
    return right_mark


def heap_sort(list_to_order):
    """
    """
    raise NotImplementedError
