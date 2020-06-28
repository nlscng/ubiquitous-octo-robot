# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a list of integers, return the largest product that can be made by multiplying any three integers.
#
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
#
# You can assume the list has at least three integers.

'''
-10, -10, 2, 5


'''


# import math
# REF: math.prod is in 3.8 and upward, at the moment I am running 3.7
# SEE: https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/
# GG: interesting

def math_product_py3_7(arr: list) -> int:
    res = 1
    for a in arr:
        res *= a
    return res


def max_product_of_three(arr: list) -> int:
    if len(arr) == 3:
        return math_product_py3_7(arr)
    arr.sort()
    max_3_prod = math_product_py3_7(arr[-3:])
    max_2_min_1_prod = math_product_py3_7([arr[-2], arr[-1], arr[0]])
    max_1_min_2_prod = math_product_py3_7([arr[-1], arr[0], arr[1]])

    return max(max_3_prod, max_2_min_1_prod, max_1_min_2_prod)


assert max_product_of_three([1, 1, 1]) == 1
assert max_product_of_three([1, 0, 3]) == 0
assert max_product_of_three([-5, 2, 1, 4]) == 8
assert max_product_of_three([-10, -3, -5, -6, -20]) == -90
assert max_product_of_three([1, -4, 3, -6, 7, 0]) == 168
