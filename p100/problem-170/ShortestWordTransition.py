# This problem was asked by Facebook.
#
# Given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence from
# start to end such that only one letter is changed at each step of the sequence, and each transformed word exists in
# the dictionary. If there is no possible transformation, return null. Each word in the dictionary have the same
# length as start and end and is lowercase.
#
# For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, return ["dog", "dot",
# "dat", "cat"].
#
# Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return null as there is no
# possible transformation from dog to cat.

"""
See pramp 1 for ideas; it's near identical with this problem, with the difference of having to track the actual paths.

A modification to bfs should be able to solve this. So instead of just tracking a queue for the frontiers of nodes
being visited, we have to keep a queue of paths that's being visited. This is why BFS loses to DFS on memory.

"""

from collections import deque


def is_one_diff(a: str, b: str) -> bool:
    assert a and b and len(a) == len(b)

    num_diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            num_diff += 1
            if num_diff > 1:
                return False

    return num_diff == 1


def bfs_shortest_transition(lex: set, src: str, tgt: str) -> list:
    assert lex and src and tgt and src in lex and tgt in lex

    # GG: important, we track a queue of paths, not just a queue of nodes, so that we can return the path soon as we
    #  find it.
    queue = deque([[src]])
    seen = set()

    while len(queue) > 0:
        one_path: list = queue.popleft()
        end = one_path[-1]
        seen.add(end)
        if end == tgt:
            return one_path

        extended_paths = [one_path + [x] for x in lex if x not in seen and is_one_diff(x, end)]
        queue.extend(extended_paths)

    return []


d1 = {'dog', 'dot', 'dop', 'dat', 'cat'}
s1 = 'dog'
t1 = 'cat'
assert bfs_shortest_transition(d1, s1, t1) == ['dog', 'dot', 'dat', 'cat']

d2 = {'dog', 'dot', 'tod', 'dar', 'cat'}
assert not bfs_shortest_transition(d2, s1, t1)
