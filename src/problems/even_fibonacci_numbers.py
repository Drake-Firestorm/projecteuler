def default_fibonacci(limit: int, result=[0, 1]) -> list:
    """Return regular fibonacci function starting at 0 upto limit."""
    value = result[-1]
    prev_value = result[-2]

    new_value = value + prev_value
    if new_value <= limit:
        result.append(new_value)
        default_fibonacci(limit=limit, result=result)
    return(result)


def fibonacci(limit: int, start=0) -> list:
    """
    Return custom fibonacci starting at any random number upto limit.
    
    The start of the series is set to
    the fibonacci number greater than equal to start number
    """
    # save default fibonacci series ending at limit
    result = default_fibonacci(limit=limit)

    # save numbers greater than equal to start
    result = [x for x in result if x >= start]

    return result


if __name__ == '__main__':
    # sum even fibonacci numbers
    x = fibonacci(limit=4e6, start=1)
    y = sum([a for a in x if a % 2 == 0])
    print(y)
