# This problem was asked by Google.
#
# We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i]
# and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.
#
# Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
#
# You may assume each element in the array is distinct.
#
# For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1),
# and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

def mergesort(arr: list):
    if not isinstance(arr, list):
        raise Exception('Expected a list, got {} instead.'.format(type(arr)))
    if not arr:
        return 0

    def divide_conqure(a: list, l: int, r: int):
        if l < r:
            m = (l + r) // 2
            divide_conqure(a[:m], l, m)
            divide_conqure(a[m+1:], m+1, r)



def count_out_of_order(arr:list):
    # the ideas is, to figure out how many "out of order" there are, we have to compare them, and since
    # we have to compare them, we could just note all the comparing that needs to be done during sorting that
    # is "out of order".
    # and there are many sorting that's better than O(n^2)
    # TODO: this is the a-ha
    pass


