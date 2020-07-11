# This problem was asked by Microsoft.
#
# Given a number in the form of a list of digits, return all possible permutations.
#
# For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

'''
1,2,3 ->



'''


def permutation(arr: list) -> list:
    if not arr:
        return []
    if len(arr) == 1:
        return [arr]

    def recur(my_arr: list):
        if len(my_arr) == 1:
            return [my_arr]

        res = []
        for idx, a in enumerate(my_arr):
            for r in recur(my_arr[:idx] + my_arr[idx + 1:]):
                res.append([a] + r)
        return res

    return recur(arr)


assert permutation([]) == []
assert permutation([3]) == [[3]]
assert permutation([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], \
    "Actual: {}".format(permutation([1, 2, 3]))
