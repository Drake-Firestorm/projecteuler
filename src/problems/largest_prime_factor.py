import math

def factors(number: int) -> list:
    """Return all factors of a number."""
    # variables
    result = list()
    
    # check if divisble by 2
    if number % 2 == 0:
        result.append(2)

    # find all factors
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            result.append(i)
    
    return result


def prime_factors(number: int) -> list:
    """Return all prime factors of a number."""
    # variables
    not_prime = list()
    result = list()

    # generate all factors
    fac = factors(number)

    # find all non primes amongst the factors
    # by checking if the factor is divisble by other factors.
    for i in fac:
        y = [x for x in fac if x != i]
        for x in y:
            if x % i == 0:
                not_prime.append(x)

    # remove all non primes from the factors
    result = [x for x in fac if x not in not_prime]

    return result


if __name__ == '__main__':
    x = prime_factors(600851475143)
    print(x)
    print(max(x))
