import pytest
from problems import largest_prime_factor as p

def test_fibonacci():
    '''Test fibonacci function.'''
    assert p.prime_factors(13195) == [5, 7, 13, 29]
