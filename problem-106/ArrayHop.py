# This problem was asked by Pinterest.
#
# Given an integer list where each number represents the number of hops you can make, determine whether you can reach
# to the last index starting at index 0.
#
# For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.


'''
1,1,0,1 -> False
    .

2,0,1,0 -> True

I think this is simply scanning through the array, skipping num of elements as we go alone, check if we can get to the
end

'''


def end_reachable(arr: list) -> bool:
    if not arr:
        return False
    if len(arr) == 1:
        return True

    n = len(arr)
    walker = 0
    while walker < n:
        if walker == n - 1:
            return True

        if arr[walker] == 0:
            return False

        walker += arr[walker]

    return False


assert end_reachable([2])
assert not end_reachable([])
assert end_reachable([2, 0, 1, 0])
assert not end_reachable([1, 1, 0, 1])
