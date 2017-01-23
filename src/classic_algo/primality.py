"""
A few simple algorithms regarding primality of numbers

"""


def sieve_of_erathosthene(n):
    """
    The sieve of Erathosthene is an efficient way to return all prime numbers up
    to an integer n. A list of boolean is created and is used as a mask:
    the index corresponds to the number and the boolean to whether its prime or
    not. As we loop over the number from 2 to sqrt(n), we set to False the
    multiple of these numbers, those remaining at True are necessarily prime.
    Note that sympy.primerange provides this functionality.
    """
    if n == 2:
        return [2, ]
    if n < 2:
        return []
    # we initialise the sieve directly to its stage after 2
    sieve = [False, False, True] + [True, False] * (n - 1) / 2
    # then we comb from 3 to sqrt(n)
    for i in range(3, ceil(n**0.5), 2):
        if sieve[i]:
            for j in range(i**2, n, i):
                sieve[j] = False
    return [i for i in range(n) if sieve[i]]


def is_prime_naive(n):
    """
    """
    raise NotImplementedError


def is_prime(n):
    """
    """
    raise NotImplementedError


def segmented_sieve_of_erathosthene():
    """
    """
    raise NotImplementedError
