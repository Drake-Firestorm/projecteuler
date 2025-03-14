import pytest
from problems import smallest_multiple as s

def test_fibonacci():
    '''Test fibonacci function.'''
    assert s.smallest_multiple(start=1, stop=10) == 2520
