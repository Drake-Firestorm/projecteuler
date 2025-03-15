import pytest
from problems import prime_10001st as p

def test_prime_numbers():
    '''Test prime number function.'''
    assert p.prime_numbers(10) == [2, 3, 5, 7]


def test_n_th_prime():
    '''Test nth prime function.'''
    assert p.n_th_prime(6) == 13
