# This problem was asked by Google.
# The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
import copy


def power_set(l: list):
    if len(l) == 0:
        return [set()]

    out = [set()]
    in_list = list(l)
    for member in in_list:
        out = helper(out, member)
    return out


def helper(l: list, new_member: int):
    group_1 = copy.deepcopy(l)
    group_2 = copy.deepcopy(l)

    # add new member to only group two
    for m in group_2:
        m.add(new_member)

    new_list = group_1 + group_2
    return new_list


def unordered_list_equal(a: list, b: list):
    if len(a) != len(b):
        return False

    for i in a:
        if i not in b:
            return False
    return True


# test
set_a = [1, 2, 3]
set_a_power = [set(), {3}, {2}, {2, 3}, {1}, {1, 3}, {1, 2}, {1, 2, 3}]

assert unordered_list_equal(power_set([]), [set()])
assert unordered_list_equal(power_set([1, 2]), [set(), {1}, {2}, {1, 2}])

assert unordered_list_equal(power_set(set_a), set_a_power)



