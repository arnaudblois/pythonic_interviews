from collections import Counter


def palindrome_permutation(string):
    """
    """
    string = string.strip().lower()
    c = Counter(string)
    l = [1 for letter_count in c.values() if letter_count % 2 == 1]
    return sum(l) < 2
