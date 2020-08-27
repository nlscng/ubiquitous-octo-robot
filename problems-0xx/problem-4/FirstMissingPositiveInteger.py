# This problem was asked by Stripe. Given an array of integers, find the first missing positive integer in linear
# time and constant space. In other words, find the lowest positive integer that does not exist in the array. The
# array can contain duplicates and negative numbers as well.


def first_missing(in_list: list):
    # this uses a list of boolean flags, so breaks the constant space requirement, but I
    # think this version is pretty cool to begin with
    if not in_list:
        return 1

    flags = [False for x in in_list]
    for i in range(len(in_list)):
        value = in_list[i]
        if 0 < value <= len(flags):
            flags[value - 1] = True

    for i in range(len(flags)):
        if not i:
            return i + 1
    return len(flags) + 1


assert first_missing([3, 4, -1, 1]) == 2
assert first_missing([1, 2, 0]) == 3
assert first_missing([1, 2, 5]) == 3
assert first_missing([1]) == 2
assert first_missing([-1, -2]) == 1
assert first_missing([]) == 1


def fist_missing_2(in_list: list):
    # this version should try to use constant space, so a lot of in place array swap?
    return None
