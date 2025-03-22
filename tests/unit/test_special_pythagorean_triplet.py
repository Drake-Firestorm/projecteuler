import pytest
from problems import special_pythagorean_triplet as p

def test_pythagorean_triplet():
    '''Test pythagorean triplet function.'''
    assert p.pythagorean_triplet(limit=5) == [(3, 4, 5)]
