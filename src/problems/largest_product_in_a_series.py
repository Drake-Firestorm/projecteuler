# library
import numpy as np

# 1000 digit number
number = str(int(
    '73167176531330624919225119674426574742355349194934' \
    '96983520312774506326239578318016984801869478851843' \
    '85861560789112949495459501737958331952853208805511' \
    '12540698747158523863050715693290963295227443043557' \
    '66896648950445244523161731856403098711121722383113' \
    '62229893423380308135336276614282806444486645238749' \
    '30358907296290491560440772390713810515859307960866' \
    '70172427121883998797908792274921901699720888093776' \
    '65727333001053367881220235421809751254540594752243' \
    '52584907711670556013604839586446706324415722155397' \
    '53697817977846174064955149290862569321978468622482' \
    '83972241375657056057490261407972968652414535100474' \
    '82166370484403199890008895243450658541227588666881' \
    '16427171479924442928230863465674813919123162824586' \
    '17866458359124566529476545682848912883142607690042' \
    '24219022671055626321111109370544217506941658960408' \
    '07198403850962455444362981230987879927244284909188' \
    '84580156166097919133875499200524063689912560717606' \
    '05886116467109405077541002256983155200055935729725' \
    '71636269561882670428252483600823257530420752963450'
))

def split_size_n(num: int, size: int) -> int:
    num = str(num)
    size = int(size)

    # list containing splits of size n
    y = list()

    # number of digits in the number
    digits = len(str(num))

    # append all digits of len size into y    
    for i in np.arange(digits):
        if i+size <= digits:
            y.append(num[i:(i+size)])

    return y


def product_digits(num: int) -> int:
    num = int(num)

    # variables
    digits = len(str(num))
    # set product to 0 if all digits are 0 else 1
    if str(num) == ('0' * digits):
        product = 0
    else:
        product = 1
    

    for i in np.arange(digits):
        multiplier = num % 10
        num = num // 10
        product = product * multiplier

    return product


def max_product(num:int, size: int) -> set:
    num = int(num)
    size = int(size)

    # variables
    products = dict()

    # find all splits of length=size
    splits = split_size_n(num, size)

    # find products for all splits
    for i in splits:
        products[i] = product_digits(i)

    # find max product from all values
    max_prod = max(products.values())
    
    # find index for max products,
    # using which find all numbers with that product
    index = [i for i, x in enumerate(products.values()) if x == max_prod]
    num_max_prod = [x for i, x in enumerate(products.keys()) if i in index]

    # return max product and all numbers with that product
    return (max_prod, num_max_prod)


if __name__ == '__main__':
    print(max_product(number, 13))
