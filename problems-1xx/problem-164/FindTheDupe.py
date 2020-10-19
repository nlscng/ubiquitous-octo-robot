# This problem was asked by Google.

# You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. By the pigeonhole
# principle, there must be a duplicate. Find it in linear time and space.

def find_the_dupe(lis: list) -> int:
    assert lis

    seen = set()
    for i in lis:
        if i not in seen:
            seen.add(i)
        else:
            return i

    raise Exception("Failed to find the dupe, this is a list of all unique members")


assert find_the_dupe([1, 2, 3, 4, 3]) == 3
