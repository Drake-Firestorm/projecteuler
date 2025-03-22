# library
import numpy as np
import itertools
from functools import reduce


def pythagorean_triplet(limit: int) -> set:
    '''
    Return all pythagorean triplets
    with each value in the triplet less than or equal to limit.
    '''
    # variabls
    result = list()

    # create range between 1 and limit
    items = np.arange(limit+1)
    
    # build all combinations from items    
    combo = list(itertools.combinations(items, 3))
    
    # if the combo is a pythagorean triplet
    # then append the combo to result
    for i in combo:
        a, b, c = list(i)
        if a**2 + b**2 == c**2:
            result.append(i)

    return result



if __name__ == '__main__':
    # variabls
    result = list()
    total = 1e3
    
    # if sum of numbers in each combo is equal to the passed value of total
    # and if the combo is a pythagorean triplet
    # then append the combo to result
    pt = pythagorean_triplet(total)

    for i in pt:
        if np.sum(i) == total:
            result.append(i)

    product = np.prod(result)
    print(result, product)
