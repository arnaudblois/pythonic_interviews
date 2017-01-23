from ..P4_palindrome_permutation import palindrome_permutation


data_true = ['', 'a', 'aa', 'aaa', 'abccba', 'ccaabb', 'abcdcba', 'aabbccd']
data_false = ['ab', 'abvdef']


def test_permutations():
    # checking strings which are palindrom permutations
    for test_string in data_true:
        assert palindrome_permutation(test_string) == True

    # strings which are not
    for test_string in data_false:
        assert palindrome_permutation(test_string) == False
