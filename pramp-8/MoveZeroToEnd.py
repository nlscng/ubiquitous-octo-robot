def move_zero_naive(arr):
    zeros = []
    not_z = []
    for one_num in arr:
        if one_num == 0:
            zeros.append(one_num)
        else:
            not_z.append(one_num)

    res = not_z + zeros
    return res


def move_zero(arr: list):
    writer = 0
    for reader in range(len(arr)):
        if arr[reader] != 0:
            arr[reader], arr[writer] = arr[writer], arr[reader]
            writer += 1

    return arr


assert move_zero([]) == []
assert move_zero([0]) == [0]
assert move_zero([1]) == [1]
assert move_zero([0,0]) == [0,0]
assert move_zero([1, 0, 2]) == [1, 2, 0]
assert move_zero([0, 0, 3]) == [3, 0, 0]
assert move_zero([1, -1, 2, 4, 6]) == [1, -1, 2, 4, 6]