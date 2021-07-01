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

def tree_max_sum_path(ar2d: []) -> int:
    # GG: this is a great question! Got me to think about DFS, back tracking, recursion, and then finally dp

    if not ar2d or not ar2d[0]:
        return []

    for r in range(1, len(ar2d)):
        for c in range(1, len(ar2d[r])):
            cur_cell = ar2d[r][c]
            last_level = ar2d[r-1][c-1] if r == c else max(ar2d[r-1][c-1], ar2d[r-1][c])
            ar2d[r][c] = cur_cell + last_level

    end_r, end_c = len(ar2d[-1]) -1, ar2d[-1].index(max(ar2d[-1]))
    my_path = [ar2d[end_r][end_c]]
    while end_r > 0:
        if end_r == end_c:
            end_c = end_c - 1
        elif ar2d[end_r - 1][end_c - 1] > ar2d[end_r-1][end_c]:
            end_c = end_c - 1
        else:
            end_c = end_c
        my_path.append(ar2d[end_r -1][end_c])
        end_r -= 1
    my_path.append(ar2d[0][0])
    my_path.reverse()
    return my_path


a = [[1],
     [2, 3],
     [1, 5, 1]]

assert tree_max_sum_path(a) == [1,3,5], "Actual: {}".format(tree_max_sum_path(a))
