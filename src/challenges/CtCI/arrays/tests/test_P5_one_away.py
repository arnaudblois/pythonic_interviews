from ..P5_one_away import is_one_letter_away


data_true = [
    ('pale', 'ale'),
    ('ale',  'pale'),
    ('pale', 'bale'),
    ('bale', 'babe'),
    ('Python', 'Jython'),
    ('Python', 'Python'),
]


data_false = [
    ('abcd', 'efgh'),
    ('pale', 'al'),
    ('dcw4f', 'dcw5fgklm'),
    ('al', 'pale'),
    ('dcw5fgklm', 'dcw4f'),
]


def test_is_one_away():
    for test_string in data_true:
        assert is_one_letter_away(*test_string) == True
    for test_string in data_false:
        assert is_one_letter_away(*test_string) == False
