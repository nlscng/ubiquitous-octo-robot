# Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that
# finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a
# substring doesn’t exist.
#
# Come up with an asymptotically optimal solution and analyze the time and space complexities.
#
# Example:
#
# input:  arr = ['x','y','z'], str = "xyyzyzyx"
#
# output: "zyx"

def get_shortest_unique_substring(arr: list, s: str) -> str:
    # safety check and stuff
    if not arr or not s:
        return ""

    is_present = {a: False for a in arr}
    count = {a: 0 for a in arr}

    def is_valid() -> bool:
        return all(is_present.values())

    shortest = s
    l_walker, r_walker = 0, 0
    count[s[r_walker]] += 1
    is_present[s[r_walker]] = True
    while l_walker < len(s) and len(s) > r_walker >= l_walker:
        if is_valid():
            found = s[l_walker: r_walker + 1]
            if len(shortest) > len(found):
                shortest = found
            count[s[l_walker]] -= 1
            if count[s[l_walker]] == 0:
                is_present[s[l_walker]] = False
            l_walker += 1   # remember to move l_walker after processing the chr at l_walker, not before
        else:
            r_walker += 1
            if r_walker < len(s):   # need to check for boundary coz we are moving right
                count[s[r_walker]] += 1
                if count[s[r_walker]] == 1:
                    is_present[s[r_walker]] = True

    return shortest


assert get_shortest_unique_substring([], "abc") == ""
assert get_shortest_unique_substring(['x'], "") == ""
assert get_shortest_unique_substring(['a'], "a") == "a"
assert get_shortest_unique_substring(['x', 'y', 'z'], "xyyzyzyx") == "zyx", "Acutal: {}".format(
    get_shortest_unique_substring(['x', 'y', 'z'], "xyyzyzyx"))
