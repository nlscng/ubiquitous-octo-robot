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

def get_shortest_unique_substring(arr: list, str: str) -> str:
    # safety check and stuff
    if not arr or not str:
        return ""

    is_present = {a: False for a in arr}
    count = {a: 0 for a in arr}

    def is_valid() -> bool:
        return all(is_present.values())

    shortest = None
    l_walker, r_walker = 0, 0
    # count[s[r_walker]] += 1
    # is_present[s[r_walker]] = True
    while l_walker < len(str) and l_walker <= r_walker <= len(str):
        if is_valid():
            found = str[l_walker: r_walker]
            if shortest is None or len(shortest) > len(found):
                shortest = found
            if str[l_walker] in count:
                count[str[l_walker]] -= 1
                if count[str[l_walker]] == 0:
                    is_present[str[l_walker]] = False
            l_walker += 1  # remember to move l_walker after processing the chr at l_walker, not before
        else:
            if r_walker < len(str) and str[r_walker] in count:  # need to check for boundary coz we are moving right
                count[str[r_walker]] += 1
                if count[str[r_walker]] == 1:
                    is_present[str[r_walker]] = True
            r_walker += 1

    return shortest if shortest is not None else ""


assert get_shortest_unique_substring([], "abc") == ""
assert get_shortest_unique_substring(['x'], "") == ""
assert get_shortest_unique_substring(['a'], "a") == "a"
assert get_shortest_unique_substring(['x', 'y', 'z'], "xyyzyzyx") == "zyx", "Acutal: {}".format(
    get_shortest_unique_substring(['x', 'y', 'z'], "xyyzyzyx"))
assert get_shortest_unique_substring(['a'], 'b') == ""
assert get_shortest_unique_substring(['a'], 'a') == 'a'
assert get_shortest_unique_substring(['A', 'B', 'C'], 'ADOBECODEBANCDDD') == 'BANC'
assert get_shortest_unique_substring(["A", "B", "C", "E", "K", "I"], 'KADOBECODEBANCDDDEI') == 'KADOBECODEBANCDDDEI'
