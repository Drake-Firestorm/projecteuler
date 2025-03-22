# Algorithm urls
# https://www.geeksforgeeks.org/sieve-of-atkin/
# https://www.baeldung.com/cs/prime-number-algorithms

# library
import numpy as np


def prime_numbers(limit: int) -> int:
    """
    Return the prime numbers smaller than limit using Sieve of Atkin.
    """
    # result list
    prime = [2, 3, 5]

    # Initialise the sieve array with initial false values
    sieve = [False] * limit

    # set 2 and 3 as True
    if limit > 2:
        sieve[2] = True
    
    if limit > 3:
        sieve[3] = True

    """
    Mark sieve[n] is true if one
       of the following is true:
    a) n = (4*x*x)+(y*y) has odd number of solutions,
        i.e., there exist odd number of distinct pairs (x, y)
            that satisfy the equation
        and n % 12 = 1 or n % 12 = 5.
    b) n = (3*x*x)+(y*y) has odd number of solutions
        and n % 12 = 7
    c) n = (3*x*x)-(y*y) has odd number of solutions,
       x > y and n % 12 = 11
    """
    for x in np.arange(1, int(np.sqrt(limit) + 1)):
        for y in np.arange(1, int(np.sqrt(limit) + 1)):
    
            # a. 4x^2 + y^2     
            n = (4 * x**2) + y**2
            if n < limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] ^= True
    
            # b. 3x^2 + y^2
            n = (3 * x**2) + y**2
            if n < limit and n % 12 == 7:
                sieve[n] ^= True
    
            # c. 3x^2 - y^2
            n = (3 * x**2) - y**2
            if n < limit and n % 12 == 11 and x > y:
                sieve[n] ^= True


    # Mark all multiples of squares as non-prime
    for i in np.arange(limit):
        if sieve[i]:
            for s in np.arange(start=i**2, stop=limit, step=i**2):
                sieve[s] = False

    # convert sieve to numbers
    prime = [x for x in np.arange(limit) if sieve[x]]
    
    # return primes
    return prime



def n_th_prime(n: int) -> int:
    x = prime_numbers(n**2)

    return x[n - 1]


if __name__ == '__main__':
    print(n_th_prime(10001))
