# This problem was asked by Amazon.
#
# Given a pivot x, and a list lst, partition the list into three parts.
#
# The first part contains all elements in lst that are less than x
# The second part contains all elements in lst that are equal to x
# The third part contains all elements in lst that are larger than x
# Ordering within a part can be arbitrary.
#
# For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].


"""
This feels like part of fast select, or the linear time median problem.

The first solution I can think of is using extra space but linear time. Create three new arrays, one for the "lessers",
one for the "equals", and one for the "greaters". Scan the incoming array and move elements into those, and concate them
at the end.

There is probably an in-place method too...
"""


def array_partition_extra_space(array: list, k: int) -> list:
    assert array
    lesser, equals, greater = [], [], []

    for a in array:
        if a < k:
            lesser.append(a)
        elif a == k:
            equals.append(a)
        else:
            greater.append(a)
    return lesser + equals + greater


assert array_partition_extra_space([1, 2, 3, 4, 5, 6], 3) == [1, 2, 3, 4, 5, 6]
assert array_partition_extra_space([2, 3, 2, 3, 2, 3], 3) == [2, 2, 2, 3, 3, 3]
assert array_partition_extra_space([9, 12, 3, 5, 14, 10, 10], 10) == [9, 3, 5, 10, 10, 12, 14]

"""
Now let me think about the in place method.
This may be reduced to a counting problem. If I count how many are smaller, equal, and greater, I can find where each 
section would start in the original array. Then this is array element swapping with 3 pointers?
"""

# GG: this is O(n) in time and O(1) in space. One possible improvement is to make this a stable sort
def array_partition(array: list, k: int) -> list:
    assert array
    n = len(array)
    ls, es, gs = 0, 0, 0    # starting index for each segment

    for a in array:
        if a < k:
            ls += 1
        elif a == k:
            es += 1
        else:
            gs += 1
    assert ls + es + gs == n
    # these are the actual starting indices
    ls, es, gs = 0, ls, ls + es
    # then these are the walking pointers
    l, e, g = ls, es, gs

    i = 0
    while i < n:
        if array[i] < k and i >= es:
            array[i], array[l] = array[l], array[i]
            l += 1
            i -= 1
        elif array[i] == k and (i < es or i >= gs):
            array[i], array[e] = array[e], array[i]
            e += 1
            i -= 1
        elif array[i] > k and i < gs:
            array[i], array[g] = array[g], array[i]
            g += 1
            i -= 1
        i += 1

    return array


assert array_partition([1, 2, 3, 4, 5, 6], 3) == [1, 2, 3, 4, 5, 6]
assert array_partition([2, 3, 2, 3, 2, 3], 3) == [2, 2, 2, 3, 3, 3]

## these tests fail because test cases assume this is a stable sort/pivot, otherwise tests would pass
print(array_partition([9, 12, 3, 5, 14, 10, 10], 10))   # == [9, 3, 5, 10, 10, 12, 14]
print(array_partition_extra_space([5,3,2,8,2,5,6,4,1,9,7,6], 5))    # == [3,2,2,4,1,5,5,8,6,9,7,6]