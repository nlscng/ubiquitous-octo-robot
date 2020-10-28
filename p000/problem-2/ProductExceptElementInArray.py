from functools import reduce
import operator


def product_other(in_list):
    """
    Given an array of integers, return a new array such that each element at index i of the new array is the product of
    all the numbers in the original array except the one at i.
    :param in_list: list of integer
    :return: a list
    """
    if len(in_list) == 0:
        return []
    else:
        product = reduce(lambda x, y: x * y, in_list)
        out = [product / i for i in in_list]
        return out


assert product_other([]) == []
assert product_other([1, 2, 3, 4]) == [24, 12, 8, 6]
assert product_other([3, 9, 7, 1]) == [63, 21, 27, 27 * 7]
assert product_other([3, 4, 5, 6]) == [120, 90, 72, 60]


# what if you can't use division?
# so without division I can't think of ways to do this in linear time yet
# right now this is O(n^2), more or less brute force
def product_other_no_division(in_list):
    if not in_list:
        return []

    return [reduce(operator.mul, in_list[:i] + in_list[i + 1:], 1) for i in range(len(in_list))]


assert product_other_no_division([]) == []
assert product_other_no_division([1, 2, 3, 4]) == [24, 12, 8, 6]
assert product_other_no_division([3, 9, 7, 1]) == [63, 21, 27, 27 * 7]
assert product_other([3, 4, 5, 6]) == [120, 90, 72, 60]


# this is not mine but from github, pretty clever
# https://github.com/vineetjohn/daily-coding-problem/blob/master/solutions/problem_002.py
def get_factors(array):
    cumulative_product = 1
    right_prod_array = list()
    for num in array:
        cumulative_product *= num
        right_prod_array.append(cumulative_product)

    cumulative_product = 1
    left_prod_array = list()
    for num in array[::-1]:
        cumulative_product *= num
        left_prod_array.append(cumulative_product)
    left_prod_array = left_prod_array[::-1]

    output_array = list()
    for i in range(len(array)):
        if i == 0:
            num = left_prod_array[i + 1]
        elif i == len(array) - 1:
            num = right_prod_array[i - 1]
        else:
            num = right_prod_array[i - 1] * left_prod_array[i + 1]
        output_array.append(num)

    return output_array


assert get_factors([]) == []
assert get_factors([1, 2, 3, 4]) == [24, 12, 8, 6]
assert get_factors([3, 9, 7, 1]) == [63, 21, 27, 27 * 7]
assert get_factors([3, 4, 5, 6]) == [120, 90, 72, 60]


# Came across this on pramp on Aug 21st

def array_of_array_products(arr):
    if len(arr) < 2:
        return []

    res = []

    # forward scan
    cur_pro = 1
    for i in range(len(arr)):
        res.append(cur_pro)
        cur_pro *= arr[i]

    cur_pro = 1
    for i in reversed(range(len(arr))):
        res[i] = res[i] * cur_pro
        cur_pro *= arr[i]

    return res


assert array_of_array_products([2, 3, 0, 982, 10]) == [0, 0, 58920, 0, 0]
assert array_of_array_products([-3, 17, 430, -6, 5, -12, -11, 5]) == [-144738000, 25542000, 1009800, -72369000,
                                                                      86842800, -36184500, -39474000, 86842800]
