"""
Module containing a few of the most typical algorithm illustrating dynamic
programming.

Naive solution of these problems would typically involve calculating every
possible combinations, leading to O(n!) time which is not manageable for even
moderate input.

These systems howver can be broken down into subproblems from which the
solution of the larger system can be derived. There is usually two approaches
to solve this type of problems:

* the bottom-up approach where we start with the simpler problem and elaborate
on them to reach the complete problem

* the top-down approach where the larger problem is broken down into
subproblems, this often leads to slightly more efficient and readable solution.

A few typical example are presented in this module
**[This section is currently under construction]**
"""


def max_subarray(array):
    """
    finds the contiguous subarray of an array which as the largest sum.
    >>> max_subarray([3, -2, 1, 5, 1, -2, 2, 4])
    12
    >>> max_subarray([3, -2, 1, 5, 1, -30, 2, 4])
    7

    It is also called Kadane's algorithm, this algo is O(n) and is considered a
    simple example of dynamic programming.
    """
    if not array:
        return 0
    maximum_ending_here = array[0]
    maximum_so_far = array[0]
    for item in array[1:]:
        # the trick comes from this line: at this point either the new item
        # starts a new sequence or contribute to continue the current sequence,
        # we select hichever case gives the best value
        maximum_ending_here = max(item, maximum_ending_here + item)
        maximum_so_far = max(maximum_so_far, maximum_ending_here)
    return maximum_so_far


def longest_common_subsequence(s1, s2):
    """
    Considering two strings s1 and s2, finds the longest subsequence in common
    >>> longest_common_subsequence('ABCDEFGH', 'WBVCNDLE')
    'BCDE'
    """
    raise NotImplementedError


def solve_knapsack(items, max_weight):
    """
    solves the knapsack problem: considering a list of an infinite numbers of
    n sort of items characterised by a weight and a value (weight_i, value_i),
    returns the list of objects that maximises the value one can put in the
    knapsack without exceeding the max_weight
    """
    raise NotImplementedError


def change_making(target, coins):
    """
    returns the minimal numbers of coins required to equal the target, or None
    if the target cannot be reached.
    """
    raise NotImplementedError
