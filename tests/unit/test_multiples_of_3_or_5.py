import pytest
from problems import multiples_of_3_or_5 as m

def test_multiples():
    '''Test multiples function.'''
    assert m.sum_multiples(3, 5, 10) == 23


def test_multiples_2():
    '''Test the alternate multiples function.'''
    assert m.multiples_2(3, 5, 10) == [0, 3, 5, 6, 9]


def test_sum_numbers():
    '''Test sum of numbers function.'''
    assert m.sum_numbers(m.multiples_2(3, 5, 10)) == 23
