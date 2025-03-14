import pytest
from problems import largest_palindrome_product as p

def test_fibonacci():
    '''Test fibonacci function.'''
    assert p.largest_palindrome_product(2) == ('9009', (99, 91))
