from ..dynamic import (
    max_subarray,
    longest_common_subsequence,
    solve_knapsack,
    change_making_bottom_up, change_making_top_down, change_making_greedy,
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


# -----------------------------------------------------
#       Change making
# -----------------------------------------------------


def test_canonical_change_making():
    """
    Tests for a "canonical" coin set, which corresponds to real-life situation.
    All changes can be returned and the greedy algorithm returns the optimal
    solution
    """
    coin_set = frozenset({1, 2, 5, 10, 20, 50, 100})
    # Testing target lower than minimum coin
    assert change_making_greedy(0, coin_set) == []
    assert change_making_bottom_up(0, coin_set) == []
    assert change_making_top_down(0, coin_set) == []
    # Testing target doable with one single coin
    assert change_making_greedy(10, coin_set) == [10]
    assert change_making_bottom_up(10, coin_set) == [10]
    assert change_making_top_down(10, coin_set) == [10]
    # Testing target doable with two coins
    assert sorted(change_making_greedy(12, coin_set)) == [2, 10]
    assert sorted(change_making_bottom_up(12, coin_set)) == [2, 10]
    assert sorted(change_making_top_down(12, coin_set)) == [2, 10]
    # Testing target reachable with 3 coins
    assert sorted(change_making_greedy(14, coin_set)) == [2, 2, 10]
    assert sorted(change_making_bottom_up(14, coin_set)) == [2, 2, 10]
    assert sorted(change_making_top_down(14, coin_set)) == [2, 2, 10]
    # Target reachable with 3 coins, all different
    assert sorted(change_making_greedy(16, coin_set)) == [1, 5, 10]
    assert sorted(change_making_bottom_up(16, coin_set)) == [1, 5, 10]
    assert sorted(change_making_top_down(16, coin_set)) == [1, 5, 10]


def test_change_making_set_without_unit():
    """
    Tests for a coin_set which do not contain 1. In this case, there exist
    changes which cannot be returned
    """
    coin_set = frozenset({5, 10, 20, 50, 100})
    # Testing target lower than minimum coin
    assert change_making_greedy(16, coin_set) == []
    assert change_making_bottom_up(16, coin_set) == []
    assert change_making_top_down(16, coin_set) == []



def test_non_canonical_change_making():
    """
    Non-canonical coin set are sets for which the greedy algorithm is not
    guaranteed to return the optimal solution.
    """
    coin_set = frozenset({1, 3, 4})
    # Test showing the failure of the grredy algorithm for a non-canonical set,
    # it does not always return the minimum result
    assert sorted(change_making_greedy(6, coin_set)) == [1, 1, 4]
    assert sorted(change_making_bottom_up(6, coin_set)) == [3, 3]
    assert sorted(change_making_top_down(6, coin_set)) == [3, 3]
    # Testing target lower than minimum coin
    assert change_making_greedy(0, coin_set) == []
    assert change_making_bottom_up(0, coin_set) == []
    assert change_making_top_down(0, coin_set) == []
    # Testing target doable with one single coin
    assert change_making_greedy(4, coin_set) == [4]
    assert change_making_bottom_up(4, coin_set) == [4]
    assert change_making_top_down(4, coin_set) == [4]
    # Testing target doable with two coins
    assert sorted(change_making_greedy(7, coin_set)) == [3, 4]
    assert sorted(change_making_bottom_up(7, coin_set)) == [3, 4]
    assert sorted(change_making_top_down(7, coin_set)) == [3, 4]
    # Testing target reachable with 3 coins
    assert sorted(change_making_greedy(11, coin_set)) == [3, 4, 4]
    assert sorted(change_making_bottom_up(11, coin_set)) == [3, 4, 4]
    assert sorted(change_making_top_down(11, coin_set)) == [3, 4, 4]
