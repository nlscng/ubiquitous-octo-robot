from functools import reduce

def product_other(list):
    """
    Given an array of integers, return a new array such that each element at index i of the new array is the product of
    all the numbers in the original array except the one at i.
    :param list: list of integer
    :return: a list
    """
    if len(list) == 0:
        return []
    else:
        product = reduce(lambda x, y: x * y, list)
        out = [product / i for i in list]
        return out


assert product_other([]) == []
assert product_other([1,2,3,4]) == [24, 12, 8, 6]
assert product_other([3,9,7,1]) == [63, 21, 27, 27*7]