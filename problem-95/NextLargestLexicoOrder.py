# Given a number represented by a list of digits, find the next greater permutation of a number, in terms of
# lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest
# value/ordering.
#
# For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,
# 1] should return [1,2,3].
#
# Can you perform the operation without allocating extra memory (disregarding the input memory)?

'''

123 -> 132

132 -> 213
 l
w

321 -> 123

1243 -> 1324

1233 -> 1323

5742 -> 7254
 *
clue: given a digit x in location y, that has to its right a number bigger than x, find in those numbers x's next
    largest number, aka the min in those numbers that are bigger than x, pull that number up to location y, and sort
    the rest.
'''


def next_largest(arr: list):
    # GG: tricky to consider everything correctly, a good question
    # this is worst case O(n log n) in time, O(1) in space
    if not arr or len(arr) == 1:
        return arr

    walker = len(arr) - 2  # this is an inclusive ptr
    last_walker = walker + 1
    found = False
    while walker >= 0:
        if arr[walker] < arr[last_walker]:
            found = True
            break
        last_walker = walker
        walker -= 1

    if not found:
        arr.reverse()
        return arr
    else:
        next_largest_val = min([a for a in arr[last_walker:] if a > arr[walker]])
        idx = arr.index(next_largest_val)
        res = arr[:walker] + [next_largest_val] + sorted([arr[walker]] + arr[last_walker:idx] + arr[idx + 1:])
        return res


assert next_largest([1, 2, 3]) == [1, 3, 2], "Actual: {}".format(next_largest([1, 2, 3]))
assert next_largest([1, 3, 2]) == [2, 1, 3], "Actual: {}".format(next_largest([1, 3, 2]))
assert next_largest([1, 2, 3, 3]) == [1, 3, 2, 3]
assert next_largest([5, 7, 4, 2]) == [7, 2, 4, 5]
