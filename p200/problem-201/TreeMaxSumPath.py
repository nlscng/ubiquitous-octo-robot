# This problem was asked by Google.
#
# You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. For
# example, [[1], [2, 3], [1, 5, 1]] represents the triangle:
#
# 1 2 3 1 5 1 We define a path in the triangle to start at the top and go down one row at a time to an adjacent
# value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the
# sum of the entries.
#
# Write a program that returns the weight of the maximum weight path.

##Review
##DP
##GOOGLE
import copy


def tree_max_sum_path(ar2d: []) -> int:
    # GG: this is a great question! Got me to think about DFS, back tracking, recursion, and then finally dp
    clone = copy.deepcopy(ar2d)
    if not ar2d or not ar2d[0]:
        return []

    for r in range(1, len(clone)):
        for c in range(len(clone[r])):
            print('({}, {})'.format(r,c))
            cur_cell = clone[r][c]
            last_level = clone[r-1][c-1] if r == c else max(clone[r-1][c-1], clone[r-1][c])
            clone[r][c] = cur_cell + last_level

    end_r, end_c = len(clone[-1]) - 1, clone[-1].index(max(clone[-1]))
    my_path = [ar2d[end_r][end_c]]
    while end_r > 0:
        if end_r == end_c:
            end_c -= 1
        elif clone[end_r - 1][end_c - 1] > clone[end_r-1][end_c]:
            end_c -= 1
        else:
            end_c = end_c
        my_path.append(ar2d[end_r - 1][end_c])
        end_r -= 1
    # my_path.append(ar2d[0][0])
    my_path.reverse()
    return my_path


a = [[1],
     [2, 3],
     [1, 5, 1]]

assert tree_max_sum_path(a) == [1,3,5], "Actual: {}".format(tree_max_sum_path(a))

b = [[1],
     [2, 3],
     [1, 5, 1],
     [1, 0, 1, 7]]
assert tree_max_sum_path(b) == [1, 3, 1, 7]
