def palindrome_product(num_1: int, num_2: int) -> int:
    """Return palindrome product of two numbers."""
    # variables
    check_palindrome = False

    # get product
    product = num_1 * num_2
    
    # check if product has even digits
    if len(str(product)) % 2 == 0:
        check_palindrome = True
    
    # find the two halfs of the product if it is an even number
    # else return 0
    if check_palindrome:
        product = str(product)
        length = int(len(product) / 2)
        left = product[:length]
        right = product[length:]; right = right[::-1]
    else:
        return 0
    
    # return product if it is a palindrome else 0
    if left == right:
        return product
    else:
        return 0


def largest_palindrome_product(digits: int) -> int:
    """
    Return largest palindrome product of two numbers of a given size.

    :param digits: The size of the two numbers
    :return: The larges palindrome product
    """
    # dict to store palindromes
    palindrome = dict()

    # find largest numbers for the given digit size
    num_1 = num_2 = 10**digits - 1

    # set limit equal to smallest number of the given digit size
    limit = 10**(digits-1)

    # run while num_1 greater than limit
    while num_1 > limit:
        x = palindrome_product(num_1, num_2)

        # if x is pallindrome
        # save in dict, with key = x and items = the numbers
        # and reduce num_2 by 1
        if x != 0:
            palindrome[x] = (num_1, num_2)
            num_2 = num_2 - 1
        
        # if x is not pallindrome and num_2 greater than limit
        # reduce num_2 by 1
        elif x == 0 and num_2 > limit:
            num_2 = num_2 - 1
        
        # reduce num_1 by 1, and set num_2 equal to new num_1
        else:
            num_1 = num_1 - 1
            num_2 = num_1
    
    # return max key (as it is the max pallindrome)
    # as well as the two numbers
    result = max(palindrome.keys())
    return result, palindrome[result]


if __name__ == '__main__':
    print(largest_palindrome_product(3))
