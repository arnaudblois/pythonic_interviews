from unittest import TestCase
import random
from ..sort import (
    bubble_sort, short_bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort, merge,
)


def test_merge():
    """ testing the merge helper function of merge_sort """
    assert merge([1], [2]) == [1, 2]
    assert merge([1, 2, 4], [3, 5]) == [1, 2, 3, 4, 5]


def test_empty():
    """sorting an empty list"""
    l1 = []
    l2 = []
    assert bubble_sort(l1.copy()) == l2
    assert short_bubble_sort(l1.copy()) == l2
    assert selection_sort(l1.copy()) == l2
    assert insertion_sort(l1.copy()) == l2
    assert merge_sort(l1.copy()) == l2


def test_single_element():
    """sorting a list of one element"""
    l1 = [1,]
    l2 = [1,]
    assert bubble_sort(l1.copy()) == l2
    assert short_bubble_sort(l1.copy()) == l2
    assert selection_sort(l1.copy()) == l2
    assert insertion_sort(l1.copy()) == l2
    assert merge_sort(l1.copy()) == l2


def test_two_elements():
    """sorting a list of two elements"""
    l1 = [2, 1]
    l2 = [1, 2]
    assert bubble_sort(l1.copy()) == l2
    assert short_bubble_sort(l1.copy()) == l2
    assert selection_sort(l1.copy()) == l2
    assert insertion_sort(l1.copy()) == l2
    assert merge_sort(l1.copy()) == l2


def test_ordered_list():
    """sorting an already ordered list"""
    l1 = [1, 2, 3, 4]
    l2 = [1, 2, 3, 4]
    assert bubble_sort(l1.copy()) == l2
    assert short_bubble_sort(l1.copy()) == l2
    assert selection_sort(l1.copy()) == l2
    assert insertion_sort(l1.copy()) == l2
    assert merge_sort(l1.copy()) == l2


def test_unordered_list():
    """sorting an unordered list"""
    l1 = [4, 2, 3, 1]
    l2 = [1, 2, 3, 4]
    assert bubble_sort(l1.copy()) == l2
    assert short_bubble_sort(l1.copy()) == l2
    assert selection_sort(l1.copy()) == l2
    assert insertion_sort(l1.copy()) == l2
    assert merge_sort(l1.copy()) == l2


def test_duplicated_list():
    """sorting an unordered list with some duplicate"""
    l1 = [4, 2, 2, 2, 3, 3, 1, 1]
    l2 = [1, 1, 2, 2, 2, 3, 3, 4]
    assert bubble_sort(l1.copy()) == l2
    assert short_bubble_sort(l1.copy()) == l2
    assert selection_sort(l1.copy()) == l2
    assert insertion_sort(l1.copy()) == l2
    assert merge_sort(l1.copy()) == l2


def test_random_against_builtin():
    """generate 10 random lists and compared them with builtin sorted"""
    for _ in range(10):
        l = random.sample(range(1, 100), 10)
        sorted_l = sorted(l)
        assert bubble_sort(l.copy()) == sorted_l
        assert short_bubble_sort(l.copy()) == sorted_l
        assert selection_sort(l.copy()) == sorted_l
        assert insertion_sort(l.copy()) == sorted_l
        assert merge_sort(l.copy()) == sorted_l
