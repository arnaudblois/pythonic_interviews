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
subproblems, and each result is memoized (ie kept in memory) to avoid
unnecessary recomputation. This approach often leads to slightly more efficient
and readable solution.

A few typical example are presented in this module.
**[This section is currently under construction]**
"""


from utils.decorators import Memoize
import math
import pdb


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
        # starts a new sequence or contributes to continue the current sequence
        # we select whichever case gives the best value
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


#------------------------------------------------------------------------------
#  Change Making algorithms
#------------------------------------------------------------------------------


def change_making_greedy(target, coin_set):
    """
    returns the minimal numbers of coins required to reach the target, or [] if
    it can't be reached. Note that this algorithm fails for special sets of
    coins called "non-canonical" sets. Most real-life sets are canonical though
    and we can use this efficient algorithm operating in
    O(target/smallest_coin).
    """
    # We sort the coins and return early the trivial results (target below the
    # minimum available coin or target already in the coin_set)
    coins = sorted(list(coin_set))
    if target < coins[0]:
        return []
    if target in coin_set:
        return [target]
    # while there is still some change to give, we select the largest coin we
    # can return to pay this remaining change. We stop when there is no coin
    # small enough to do this
    still_to_give = target
    coins_to_use = []
    while still_to_give >= coins[0]:
        max_usable_coin = max(coin for coin in coins if coin <= still_to_give)
        still_to_give -= max_usable_coin
        coins_to_use.append(max_usable_coin)
    # if we managed to give the exact change, we return the coins we used
    return coins_to_use if still_to_give == 0 else []


def change_making_bottom_up(target, coin_set):
    """
    returns the minimal numbers of coins required to reach the target, or []
    if the target cannot be reached.
    """
    # We sort the coins and return the trivial results (target below the
    # minimum available coin or target already in the coin_set)
    coins = sorted(list(coin_set))
    if target < coins[0]:
        return []
    if target in coin_set:
        return [target]

    # Init two lists to store the minimum number of coins and their nature,
    # the index being the change_required
    coin_count = [0] * (target + 1)
    best_combo = [[] for _ in range(target + 1)]

    # Looping over the smallest coin up to the target
    for change in range(coins[0], target + 1):
        # we return faster if the change is a coin within the coin_set
        if change in coin_set:
            coin_count[change], best_combo[change] = 1, [change]
            continue
        # otherwise we locate the minimum number of coins by finding the coin
        # which added to change - coin is optimal
        minimum_number = math.inf
        minimum_coin = None
        for coin in coins:
            is_minimum = (
                change > coin and coin_count[change - coin] != 0 and
                coin_count[change - coin] + 1 < minimum_number
            )
            if is_minimum:
                minimum_number = coin_count[change - coin] + 1
                minimum_coin = coin

        # If we found a minimum coin we update the best_combo and coin_count
        # (this may not be the case for some sets not containing 1)
        if minimum_coin:
            best_combo[change] = (best_combo[change - minimum_coin] +
                                   [minimum_coin])
            coin_count[change] = coin_count[change - minimum_coin] + 1

    return best_combo[target]


@Memoize
def change_making_top_down(target, coin_set):
    """
    returns the minimal numbers of coins required to equal the target, or []
    if the target cannot be reached. Note that the coin_set has to be of type
    set or frozenset since we use memoization: the arguments must be hashable
    and a list is not.
    """
    # We sort the coins and return the trivial results (target below the
    # minimum available coin or target already in the coin_set)
    coins = sorted(list(coin_set))
    if target < coins[0]:
        return []
    if target in coin_set:
        return [target]

    # we initiate a list representing the combination giving the minimum change
    # we then loop over each coin to find if adding this coin to the ways of
    # returning target - coin leads to a new minimum
    best_combo = [0] * (target // coins[0] + 1)
    for coin in coins:
        if target - coin < 0:
            continue
        combo = change_making_top_down(target - coin, coin_set) + [coin]
        if len(combo) < len(best_combo):
            best_combo = combo
    # we make sure we have reached the target before returning the combo
    return best_combo if sum(best_combo) == target else []
