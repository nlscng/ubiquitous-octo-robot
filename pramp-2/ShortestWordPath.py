# Given two words source and target, and a list of words words, find the length of the shortest series of edits that
# transforms source to target.
#
# Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must
# exist in words.
#
# If the task is impossible, return -1.

def shortest_word_path(source, target, words):
    """
    @param source: str
    @param target: str
    @param words: str[]
    @return: int
    """

    neighbor = [word for word in words if is_one_diff(word, source)]
    queue = [(n, 1) for n in neighbor]
    words = [word for word in words if word not in neighbor]
    ptr = (None, 0)

    # found the word, or not having possible neighbors from dictionary
    while ptr[0] != target and len(queue) > 0:
        ptr = queue.pop()  # first neighbor in queue
        neighbor = [word for word in words if is_one_diff(word, ptr[0])]
        words = [word for word in words if word not in neighbor]
        queue = queue + [(n, ptr[1] + 1) for n in neighbor]

    return ptr[1] if ptr[0] == target else -1


def is_one_diff(word_a, word_b):
    if len(word_a) != len(word_b):
        return False

    diff_count = 0
    for i in range(len(word_a)):
        if word_a[i] != word_b[i]:
            diff_count += 1

    return True if diff_count == 1 else False


src = "bit"
snk = "dog"
word_bank = ["but", "put", "big", "pot", "pog", "dog", "lot"]
assert shortest_word_path(src, snk, word_bank) == 5
assert shortest_word_path("no", "go", ["to"]) == -1
assert shortest_word_path("bit", "pog", ["but","put","big","pot","pog","pig","dog","lot"]) == 3
assert shortest_word_path("aa", "bb", ["ab","bb"]) == 2
assert shortest_word_path("abc", "ab", ["abc","ab"]) == -1
assert shortest_word_path("aa", "bbb", ["ab","bb"]) == -1
