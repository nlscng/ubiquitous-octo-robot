# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each
# subarray of length k.
#
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
#
# 10 = max(10, 5, 2) 7 = max(5, 2, 7) 8 = max(2, 7, 8) 8 = max(7, 8, 7) Do this in O(n) time and O(k) space. You can
# modify the input array in-place and you do not need to store the results. You can simply print them out as you
# compute them.

FLIP_SIGN = -1


def find_max_in_subarray(liz: list, k: int):
    # this is tougher than I realized to achieve O(n)
    # my best without looking up is with a priority queue or some other max-heap type thing, but that is O(n log n)
    assert len(liz) >= k, "length of list needs to be at least k."

    import heapq

    # TODO: incomplete and wrong, this pops the max but we don't need it to pop the max unless max is outside of the window
    heap = []
    heapq.heapify(heap)
    windowed_max = []
    for i in range(len(liz)):
        if i < k - 1:
            heap.append(liz[i] * FLIP_SIGN)
            continue

        heapq.heappush(heap, liz[i] * FLIP_SIGN)
        from_heap = heapq.heappop(heap) * FLIP_SIGN
        windowed_max.append(from_heap)

    return windowed_max


# assert find_max_in_subarray([5, 2, 1], 2) == [5, 2]
# assert find_max_in_subarray([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8], "actual value is: {}".format(find_max_in_subarray([10, 5, 2, 7, 8, 7], 3))


def find_max_in_subarray_ver2(liz: list, k: int):
    # see this https://stackoverflow.com/questions/8031939/finding-maximum-for-every-window-of-size-k-in-an-array

    assert len(liz) >= k, "length of list needs to be at least k."

    left_mapped = []
    right_mapped = []
    cur_left_max, cur_right_max = 0, 0
    for i in range(len(liz)):
        if i % k == 0:
            cur_left_max, cur_right_max = 0, 0
        cur_left_max = max(cur_left_max, liz[i])
        left_mapped.append(cur_left_max)

        cur_right_max = max(cur_right_max, liz[-i - 1])
        right_mapped.append(cur_right_max)

    right_mapped.reverse()

    max_liz = []
    for i in range(len(liz) - k + 1):
        max_liz.append(max(right_mapped[i], left_mapped[i + k - 1]))

    return max_liz


assert find_max_in_subarray_ver2([5, 2, 1], 2) == [5, 2], "actual value is: {}".format(
    find_max_in_subarray_ver2([5, 2, 1, 2], 2))
assert find_max_in_subarray_ver2([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8], "actual value is: {}".format(
    find_max_in_subarray_ver2([10, 5, 2, 7, 8, 7], 3))
