from ..dynamic import (
    max_subarray,
    longest_common_subsequence,
    solve_knapsack,
    change_making,
)


# -----------------------------------
#           max subarray
# ----------------------------------

def test_max_subarray():
    # Empty array (by convention, the sum of an empty array is 0)
    assert max_subarray([]) == 0
    # Single element
    assert max_subarray([3]) == 3
    # Only negative elements
    assert max_subarray([-4, -1, -2]) == -1
    # Only positive elements
    assert max_subarray([1, 2, 3, 4, 5]) == 15
    # Mix of positive and negative, running sequence
    assert max_subarray([3, -2, 1, 5, 1, -2, 2, 4]) == 12
    # Mix of positive and negative, broken sequence
    assert max_subarray([3, -22, 1, 5, 1, -32, 2, 4]) == 7
