"""
Tests for problem P1

As mentioned in the docstring of P1_triple_steps, this problem admits the
Tribonacci sequence as answer.
The first two zeros are convention and would correspond to the N of -2 and -1
We exclude them from our tests since they do not represent a real world
situation
"""

from ..P1_triple_step import (
    tribonacci_number, triple_step_iterative,
    triple_step_bottom_up, triple_step_top_down,
)

sequence = [
    0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768,
    10609, 19513, 35890, 66012, 121415, 223317, 410744, 755476, 1389537,
    2555757, 4700770, 8646064, 15902591, 29249425, 53798080, 98950096,
    181997601, 334745777, 615693474, 1132436852,
]
L = len(sequence) - 2


def test_tribonacci_number():
    assert [tribonacci_number(N) for N in range(L)] == sequence[2:]


def test_triple_step_iterative():
    assert [triple_step_iterative(N) for N in range(L)] == sequence[2:]


def test_triple_step_bottom_up():
    assert [triple_step_bottom_up(N) for N in range(L)] == sequence[2:]


def test_triple_step_top_down():
    assert [triple_step_top_down(N) for N in range(L)] == sequence[2:]
