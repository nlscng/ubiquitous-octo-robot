# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.


def str_to_int_list(s: str):
    return [int(x) for x in s]


def num_decode_first_draft(array: list):
    ## this turns out to be wrong, adding a digit where last number is 1 (or 2 with current being <= 6) doesn't
    ## just add one more way to ways to decode, it multiplies
    if len(array) == 1 or len(array) == 0:
        return 1

    k = [1]  # let k(i) be the number of ways the array can be decoded up to the i-element; init k(0) be 1
    for i in range(1, len(array)):
        # skipping the first element, we start with idx 1
        if array[i - 1] == 1:
            k.append(k[i - 1] + 1)
        elif array[i - 1] == 2 and array[i] <= 6:
            k.append(k[i - 1] + 1)
        else:
            k.append(k[i - 1])

    return k[-1]


def num_decode(li: list):
    # the correct dynamic programming way, kinda
    # let k(i) be the number of ways the array can be decoded up to the i-element;
    # k(0) init to 1, k(1) init to 1 or 2, depending on if the first two digits makes a letter together
    # then new digit i-th, k(i) = 1 * k(i - 1) + is_a_letter( list[i-1 : i+1] ) * k(i - 2)

    if len(li) == 1 or len(li) == 0:
        return 1

    k = [1]

    def pred(arr):
        assert len(arr) > 1
        return arr[0] == 1 or (arr[0] == 2 and arr[1] <= 6)

    # init the the 2nd cell
    k.append(2) if pred(li[:2]) else k.append(1)

    for i in range(2, len(li)):
        if pred(li[i - 1:i + 1]):
            k.append(1 * k[i - 2] + 1 * k[i - 1])
        else:
            k.append(1 * k[i - 1])

    return k[-1]


assert num_decode(str_to_int_list("81")) == 1
assert num_decode(str_to_int_list("11")) == 2
assert num_decode(str_to_int_list("111")) == 3
assert num_decode(str_to_int_list("1111")) == 5
assert num_decode(str_to_int_list("1311")) == 4

assert num_decode([1, 1, 1]) == 3
assert num_decode([1, 2, 3, 4]) == 3
assert num_decode([5, 2, 4]) == 2
assert num_decode([3, 2, 1, 3, 2, 1]) == 6
assert num_decode([2, 3, 2, 3, 2, 3]) == 8
