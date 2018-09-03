from math import isclose


def test_arithmetic():
    assert 1 == 1
    assert 2 * 3 == 6

def test_len_list():
    lst = ['a', 'b', 'c']
    assert len(lst) == 3

def test_sum():
    assert 1 + 2 == 3

def test_sum_float():
    assert isclose(1.1 + 2.2, 3.3)
