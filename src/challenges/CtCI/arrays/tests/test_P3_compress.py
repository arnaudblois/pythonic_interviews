from ..P6_string_compression import compress, uncompress


# Testing the compress function
# --------------------------------

def test_compress_empty():
    assert compress('') == ''

def test_compress_one_element():
    assert compress('a') == 'a'

def test_compressible_3():
    assert compress('aaa') == 'a3'

def test_non_compressible_2():
    """ string would not be shorter after compression -> returns original """
    assert compress('aa') == 'aa'

def test_compressible_long_string():
    assert compress('abbbbbbbbbbbccccc') == 'a1b11c5'

def test_uncompressible_long_string():
    assert compress('aabbccddeeffgg') == 'aabbccddeeffgg'


# Testing the uncompress function
# --------------------------------

def test_uncompress_long_string():
    assert uncompress('a1b11c5') == 'abbbbbbbbbbbccccc'

def test_uncompress_empty():
    assert uncompress('') == ''

def test_uncompress_one_element():
    assert uncompress('a') == 'a'

def test_uncompress_one_group():
    assert uncompress('a3') == 'aaa'

def test_uncompress_no_compression():
    assert uncompress('aa') == 'aa'
    assert uncompress('helloWorld') == "helloWorld"
