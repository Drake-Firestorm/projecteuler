import pytest
from problems import sum_square_difference as s

def test_sum_squares():
    '''Test sum_squares function.'''
    assert s.sum_squares(start=1, stop=10) == 385


def test_squares_sum():
    '''Test sum_squares function.'''
    assert s.squares_sum(start=1, stop=10) == 3025


def test_difference_sum_squares():
    '''Test sum_squares function.'''
    assert s.difference_sum_squares(start=1, stop=10) == 2640
