from ..P2_check_permutations import check_permutation

data_true = [
    ('abcd', 'bacd'),
    ('3563476', '7334566'),
    ('wef34f', 'wffe34')
]

data_false = [
    ('abcd', 'd2cba'),
    ('2354', '1234'),
    ('dcw4f', 'dcw5f')
]


def test_permutations():
    # test all strings yielding True
    for test_string in data_true:
        assert check_permutation(*test_string)
    #  test strings yielding False
    for test_string in data_false:
        assert check_permutation(*test_string) is False
