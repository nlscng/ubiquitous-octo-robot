# Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four
# numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending
# order. If such a quadruplet doesn’t exist, return an empty array.
#
# Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you
# encounter (considering the results are sorted).
#
# Explain and code the most efficient solution possible, and analyze its time and space complexities.
#
# Example:
#
# input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20
#
# output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
#                      # whose sum is 20. Notice that there
#                      # are two other quadruplets whose sum is 20:
#                      # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
#                      # asked to return the just one quadruplet (in an
#                      # ascending order)


def find_array_quadruplet(arr, s):
    def sum_of_two(liz, sum):
        diff = set()
        for i in range(len(liz)):
            if liz[i] in diff:
                return [sum - liz[i], liz[i]]
            diff.add(sum - liz[i])
        return None

    def sum_of_three(liz, sum):
        for i in range(len(liz)):
            pair = sum_of_two(liz[i + 1:], sum - liz[i])
            if pair:
                a, b = pair
                return [liz[i], a, b]

        return None

    arr.sort()

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            pair = sum_of_two(arr[j + 1:], s - arr[i] - arr[j])
            if pair:
                a, b = pair
                return [arr[i], arr[j], a, b]

    return []


assert find_array_quadruplet([], 12) == []
assert find_array_quadruplet([4, 4, 4], 12) == []
assert find_array_quadruplet([4, 4, 4, 4], 16) == [4, 4, 4, 4]
assert find_array_quadruplet([0, 4, 7, 9], 20) == [0, 4, 7, 9]
assert find_array_quadruplet([2, 4, 7, 0, 9, 5, 1, 3], 20) == [0, 4, 7, 9]
assert find_array_quadruplet([2, 4, 7, 0, 9, 5, 1, 3], 120) == []
assert find_array_quadruplet([1, 2, 3, 4, 5, 9, 19, 12, 12, 19], 40) == [4, 5, 12, 19]
