import numpy as np
import largest_prime_factor as lpf

def exponent(num: int, limit: int) -> int:
    """
    Return the largest number to its exponent which is less than equal to limit.
    
    :num: Base number
    :limit: Limit of the solution
    :return: Solution of number to the power
    """
    # variables
    power = 0

    # find largest power for number
    # by incrementing power till number^power > limit
    while num**power < limit:
        power = power + 1
    
    # decrease power by 1
    # since while loop will result in 1 extra loop
    power = power - 1
    
    return num**power


def product(start: int, stop: int) -> int:
    """Return product of all numbers from start to stop, both inclusive."""
    range = np.arange(start, stop + 1)
    prod = np.prod(range)

    return prod


def smallest_multiple(start: int, stop: int) -> int:
    """Return smallest multiple of all numbers between start and stop."""
    # find product of all numbers between start and stop
    prod = product(start, stop)
    
    # find all prime factors of the product
    pf = lpf.prime_factors(prod)

    # find largest number^exponents less than stop for all prime fators
    exp = list()
    for n in pf:
        exp.append(exponent(n, stop))

    # return product of exponents
    return np.prod(exp)


if __name__ == '__main__':
    print(smallest_multiple(1, 20))
