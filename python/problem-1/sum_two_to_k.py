

def sum_two_from_list(list, sum):
    """
    :param list: a list of integer
    :param sum: a integer
    :return: True if there are two element in the list that add up to the sum
    """
    if len(list) == 0 or len(list) == 1:
        return False
    else:
        seen = set()
        for i in list:
            if i in seen:
                return True
            else:
                seen.add(sum - i)

        return False


assert sum_two_from_list([], 3) == False
assert sum_two_from_list([1], 3) == False
assert sum_two_from_list([1, 2, 3, 4, 5, 6, 7], -3) == False
assert sum_two_from_list([-2, -5, 3, 8], -2) == True

assert sum_two_from_list([1, 2, 3, 4, 5, 6, 7], 10) == True
assert sum_two_from_list([1, 3, 6, 7, 15], 10) == True


