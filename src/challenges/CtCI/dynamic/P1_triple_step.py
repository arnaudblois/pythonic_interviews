"""
Problem 1 of Chapter 8 in CtCi
Triple Step: A child is running up a staircase with N steps and can hop either
1 step, 2 steps, or 3 steps at a time. Return the number of possible ways exist
this can be done.

General idea of the solution: At any step N, the child must necessarily come
from the steps N-3, N-2 or N-1. The possible ways to go to N are therefore the
sums of the possible ways to come to N-3, N-2 and N-1. This is the definition
of the tribonacci numbers, a generalization of the Fibonacci sequence.
"""


from src.utils.decorators import Memoize


def tribonacci_number(N):
    """
    Closed-form formula to calculate the Nth Tribonacci number. Of course, no
    one would expect this in an interview :)
    """
    a1 = (19 + 3 * 33**0.5)**(1 / 3)
    a2 = (19 - 3 * 33**0.5)**(1 / 3)
    b = (586 + 102 * 33**0.5)**(1 / 3)
    numerator = 3 * b * (1 / 3 * (a1 + a2 + 1))**(N + 1)
    denominator = b**2 - 2 * b + 4
    result = round(numerator / denominator)
    return result


def triple_step_iterative(nb_of_steps):
    """
    The most naive implementation, using 3 variables corresponding
    to the 3 previous states, we calculate the next and update them
    continuously until we've looped up to nb_of_steps.
    """
    a, b, c = 0, 0, 1
    for step in range(nb_of_steps):
        temp_var = a + b + c
        a = b
        b = c
        c = temp_var
    return c


def triple_step_bottom_up(nb_of_steps):
    """
    As with all bottom-up approaches, we initiate a list which we
    update as we calculate the next step.
    """
    nb_possible_ways = [1, 1, 2] + [None for _ in range(3, nb_of_steps + 1)]
    for step in range(3, nb_of_steps + 1):
        nb_possible_ways[step] = (
            nb_possible_ways[step - 1]
            + nb_possible_ways[step - 2]
            + nb_possible_ways[step - 3]
        )
    return nb_possible_ways[nb_of_steps]


@Memoize
def triple_step_top_down(nb_of_steps):
    """
    In the top-down approach, the problem is broken down into easier
    problems: solving for N corresponds to solving for N-1, N-2 and
    N-3 and adding them. The use of memoization avoids recomputation.
    """
    if nb_of_steps == 0:
        return 1
    if nb_of_steps in [1, 2]:
        return nb_of_steps
    return (
        triple_step_top_down(nb_of_steps - 1)
        + triple_step_top_down(nb_of_steps - 2)
        + triple_step_top_down(nb_of_steps - 3)
    )
