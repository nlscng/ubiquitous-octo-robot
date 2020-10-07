# A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a
# pre-shifted copy of it. For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to
# the left.
#
# Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in
# shiftArr. If num isn’t in shiftArr, return -1. Assume that the offset can be any value between 0 and arr.length - 1.
#
# Explain your solution and analyze its time and space complexities.
#
# Example:
#
# input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
#                                                  # outcome of shifting
#                                                  # [2, 4, 5, 9, 12, 17]
#                                                  # three times to the left
#
# output: 3 # since it’s the index of 2 in arr

"""
navie:
  find num time shift

round 2:
  modified binary search for k:
    s: (starting of sorted array)
      m : take a mid (which is random value)


   two scenario:
    use m and two end points to tell which scenario
    s on left half:
      k on left:
        k > begin of sub or k < m
      k on right:
        m < k < right end
    s on right half:
      k on left:
        left begin < k < m
      k on right:
        k > m or k < right end


[9, 12, 17, 2, 4, 5], k = 2
len = 6
m = 3
le = 2
re = 5




"""


def shifted_arr_search(shiftArr, num):
    # sanity check

    n = len(shiftArr)
    a = shiftArr
    le, m, re = 0, (n - 1) // 2, n - 1  # these are indices

    while le <= re:  # check conditions
        if num == a[m]:
            return m
        if a[le] > a[m]:
            # s is on left half
            if num >= a[le] or num <= a[m]:
                re = m - 1
                m = le + (re - le) // 2
            else:
                le = m + 1
                m = le + (re - le) // 2
        else:
            # s is on the right half
            if a[le] <= num <= a[m]:
                re = m - 1
                m = le + (re - le) // 2
            else:
                le = m + 1
                m = le + (re - le) // 2

    return -1


assert shifted_arr_search([2], 2) == 0
assert shifted_arr_search([1, 2], 2) == 1
assert shifted_arr_search([0, 1, 2, 3, 4, 5], 1) == 1
assert shifted_arr_search([1, 2, 3, 4, 5, 0], 0) == 5
assert shifted_arr_search([9, 12, 17, 2, 4, 5], 17) == 2
assert shifted_arr_search([9, 12, 17, 2, 4, 5, 6], 4) == 4
