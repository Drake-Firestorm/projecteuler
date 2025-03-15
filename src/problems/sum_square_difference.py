import numpy as np
from problems.multiples_of_3_or_5 import sum_numbers

def sum_squares(stop: int, start: int =1) -> int:
    """
    Sum of squares of numbers in range.

    :param start: The first number in series
    :param stop: The last number
    :return: Sum of squares of all numbers between start and stop
    """
    x = [x**2 for x in np.arange(start=start, stop=stop+1)]
    return sum_numbers(x)


def squares_sum(stop: int, start: int =1) -> int:
    """
    Square of sum of numbers in range.

    :param start: The first number in series
    :param stop: The last number
    :return: Square of sum of all numbers between start and stop
    """
    return sum_numbers(np.arange(start=start, stop=stop+1))**2


def difference_sum_squares(stop: int, start: int =1) -> int:
    """
    Return difference of square of sum of numbers and
    sum of squares of numbers in range.
    """
    sum = sum_squares(start=start, stop=stop)
    square = squares_sum(start=start, stop=stop)

    return square - sum


if __name__ == '__main__':
    # sum even fibonacci numbers
    print(difference_sum_squares(100))
