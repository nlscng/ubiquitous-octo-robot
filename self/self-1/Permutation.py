# Given a list of unique integers, return all possible permutation of this list
from itertools import permutations


def my_permu(liz: []):
    if not liz:
        return [()]

    output = []

    def helper(arr: (), left: []):
        if not left:
            output.append(arr)
            return
        for i in range(len(left)):
            one_ele = left[i]
            rest = left[:i] + left[i + 1:]
            next_arr = arr + (one_ele,)
            helper(next_arr, rest)

    helper((), liz)
    return output


assert my_permu([]) == [()], 'Actual output: {}'.format(my_permu([]))
assert my_permu([1]) == [(1,)], 'Actual output: {}'.format(my_permu([1]))
assert all(x in my_permu([1, 2]) for x in permutations([1, 2])), 'Actual output: {}'.format(
    my_permu([1, 2]))
assert all(x in my_permu([1, 2, 3]) for x in permutations([1, 2, 3])), 'Actual output: {}'.format(
    my_permu([1, 2, 3]))
