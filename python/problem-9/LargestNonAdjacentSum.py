# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0
# or negative.
#
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
# since we pick 5 and 5.
#
# Follow-up: Can you do this in O(N) time and constant space?


def find_max_sum_out_of_two(in_list: list):
    # first attempt, I didn't read the question right,
    # ended up finding a max sum of two non adjacent numbers from list
    if len(in_list) < 2:
        return 0

    cur_max = float("-inf")
    for i in range(2, len(in_list)):
        cur_max = max(cur_max, in_list[i - 2])
        in_list[i - 2] = cur_max + in_list[i]

    max_sum = max(in_list[:-2])
    return max_sum


assert find_max_sum_out_of_two([]) == 0
assert find_max_sum_out_of_two([1]) == 0
assert find_max_sum_out_of_two([2, 4, 6, 2, 5]) == 11
assert find_max_sum_out_of_two([5, 1, 1, 5]) == 10


def find_sum(in_list):
    return None


# assert find_sum([]) == 0
# assert find_sum([1]) == 0
# assert find_sum([2, 4, 6, 2, 5]) == 13
# assert find_sum([5, 1, 1, 5]) == 10
