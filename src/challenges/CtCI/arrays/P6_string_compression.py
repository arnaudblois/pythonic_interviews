
"""
Problem 1.6
compress a string by having subsequent identical characters transformed like so
hhhhh -> h5. If the string is no shorter, keep it unchanged
>>>  compress(qqqwwwwweerty)
q3w5e2t1y1

Trivia: oddly enough there a word in English with three consecutive
identical letters but none for which this compression would yield a shorted
result (closest to succeed is 'aaaaba', some sort of bee)
(https://en.wikipedia.org/wiki/List_of_words_in_English_with_tripled_letters)
>>>  compress(aaaaba)
aaaaba
"""
import re

def compress(string):
    """
    """
    if string == '':
        return ''
    compressed_string = ''
    previous_letter, count = string[0], 0
    for letter in string:
        if letter == previous_letter:
            count += 1
        else:
            compressed_string += previous_letter + str(count)
            previous_letter = letter
            count = 1
    compressed_string += letter + str(count)

    if len(compressed_string) >= len(string):
        return string
    else:
        return compressed_string


def uncompress(string):
    """
    """
    compressed_string_regex = re.compile("([a-zA-Z])(\d+)+")
    matches = compressed_string_regex.finditer(string)
    uncompressed_string = ''
    for match in matches:
        letter, repetitions = match.groups()[0], int(match.groups()[1])
        uncompressed_string += letter * repetitions
    if not uncompressed_string:
        return string
    return uncompressed_string
