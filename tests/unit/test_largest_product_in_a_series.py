# library
import pytest
from problems import largest_product_in_a_series as l


# variables
x = '641100001146'
y = '8399879790879'
z = '5576689664895'

def test_split_size_n():
    '''Test split size function.'''
    assert l.split_size_n(x, 4) == [
        '6411', '4110', '1100', '1000', '0000'
        , '0001', '0011', '0114', '1146'
    ]


def test_product_digits():
    '''Test product of digits function'''
    assert l.product_digits(x) == 0
    assert l.product_digits(y) == 0
    assert l.product_digits(z) == 23514624000


def test_max_product():
    '''Test max product function'''
    assert l.max_product(x, 4) == (24, ['6411', '1146'])
