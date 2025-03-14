import pytest
from problems import even_fibonacci_numbers as f

def test_fibonacci():
    '''Test fibonacci function.'''
    assert f.fibonacci(limit=100, start=1) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
