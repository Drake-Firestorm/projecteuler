# library
import numpy as np

# method 1
def multiples(num: int, stop_limit: int) -> list:
    """
    Return multiples of a number upto limit.
    
    :param num: The multiplicand
    :param stop_limit: The upper limit of the product
    :return: List of all multiples
    """
    return np.arange(stop=stop_limit, step=num, dtype=int)


def sum_numbers(nums: list) -> int:
    """
    Return sum of numbers.

    :param num: List of numbers
    :return: Sum of the numbers
    """
    return np.sum(nums)


def sum_multiples(num_1: int, num_2: int, stop_limit: int) -> int:
    """
    Get sum of unique multiples of two numbers.
    
    :param num_1: The first number
    :param num_2: The second number
    :param stop_limit: The upper limit of the product
    :return: Sum of the numbers
    """
    # multiples of number 1
    mul_1 = multiples(num=num_1, stop_limit=stop_limit)
    sum_1 = sum_numbers(mul_1)
    
    # multiples of 5
    mul_2 = multiples(num=num_2, stop_limit=stop_limit)
    sum_2 = sum_numbers(mul_2)
    
    # multiples of 15
    mul_3 = multiples(num=(num_1 * num_2), stop_limit=stop_limit)
    sum_3 = sum_numbers(mul_3)
    
    # return
    return sum_1 + sum_2 - sum_3


# method 2
def multiples_2(num_1: int, num_2: int, stop_limit: int) -> list:
    """
    Return all multiples of two numbers.
    
    :param num_1: The first number
    :param num_2: The second number
    :return: List of all unique multiples
    """
    x = [
            x for x in range(stop_limit)
            if x % num_1 == 0 or x % num_2 == 0
        ]
    
    return x


if __name__ == '__main__':
    print("method 1", sum_multiples(3, 5, 1000))
    print("method 2", sum_numbers(multiples_2(3, 5, 1000)))
