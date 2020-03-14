# This problem was asked by Amazon.
#
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct
# characters.
#
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


def longest_substring_k_distinct(s: str, k: int):
    if not s:
        return ""

    if len(set(s)) < k:
        return ""

    # memo for begining index i for the substring from i to this element which has at most k distinct characters.
    begin_sub_idx = [-1] * len(s)
    begin_sub_idx[0] = 0
    count = {s[0]: 1}  # init the letter count dictionary
    for i in range(1, len(s)):
        char = s[i]
        cur = begin_sub_idx[i - 1]
        # add this char to count
        if char not in count.keys():
            count[char] = 1
        else:
            count[char] += 1

        while len(count.keys()) > k:
            char_del = s[cur]
            cur += 1
            count[char_del] -= 1
            if count[char_del] == 0:
                count.pop(char_del)

        begin_sub_idx[i] = cur

    # find the longest substring by finding biggest diff from last_idx to its element
    len_sub = [i - begin_sub_idx[i] for i in range(len(begin_sub_idx))]

    out = ""
    max_len = 0
    for i in range(len(begin_sub_idx)):
        diff = i - begin_sub_idx[i]
        if diff > max_len:
            out = s[i - diff: i + 1]
            max_len = diff

    return out


assert longest_substring_k_distinct("abcba", 2) == "bcb"
assert longest_substring_k_distinct("aabbcc", 1) == "aa"
assert longest_substring_k_distinct("aabbcc", 2) == "aabb"
assert longest_substring_k_distinct("aaabbb", 3) == ""
assert longest_substring_k_distinct("aabacbebebe", 3) == "cbebebe"
