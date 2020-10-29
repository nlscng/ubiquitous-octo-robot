# Given a graph, fully connected without islands, determine if it is a bipartite

"""
During the interview session, I said this is essentailly a 2-color k-coloring problem, and I tried to solve it that way

The interviewer asked me what are the two common ways of representing a graph, and asked me which one would be better
for this problem. I didn't pick one just yet, but I did later when I realize I will be querying a node's neighbor
pretty often.

I made a small mistake at first, didn't check with the interviewer if the graph is one fully connected graph,
so I started out wanting to spin through all nodes. He then clarified that it's one fully connected graph.

So my solution became this, dfs through the grpah, try label a node a color, if that doesn't work (because this node
has a neighbor already in that golor group), try the other color. If that fails, then this is not a bipartite


"""


# SEE: https://www.geeksforgeeks.org/bipartite-graph/ for bfs solution to this.


def dfs_check(g: dict) -> bool:
    assert g
    a = set()
    b = set()

    stack = [list(g.keys())[0]]
    seen = set()
    while len(stack) > 0:
        walker = stack.pop()
        if walker not in seen:
            seen.add(walker)
            neighbors = g[walker]
            if neighbors:
                stack.extend(neighbors)

            if any([x for x in g[walker] if x in a]):
                if any([x for x in g[walker] if x in b]):
                    return False
                else:
                    b.add(walker)
            else:
                a.add(walker)
    return True


# a - b
#  \ /
# c - d
g1_true = {
    'a': ['b', 'd'],
    'b': ['c', 'a'],
    'c': ['b', 'd'],
    'd': ['a', 'c']
}

assert dfs_check(g1_true)

# a - b
#     |
# c - d
g2_true = {
    'a': ['b'],
    'b': ['d', 'a'],
    'c': ['d'],
    'd': ['b', 'c']
}
assert dfs_check(g2_true)

# a - b
# |   |
# c - d
g3_true = {
    'a': ['b', 'c'],
    'b': ['d', 'a'],
    'c': ['d', 'a'],
    'd': ['b', 'c']
}
assert dfs_check(g3_true)

# a - b
# | /
# c
g4_false = {
    'a': ['b', 'c'],
    'b': ['c', 'a'],
    'c': ['b', 'a']
}
assert not dfs_check(g4_false)

# a - b
#   \
# c - d
g5_true = {
    'a': ['b', 'd'],
    'b': ['a'],
    'c': ['d'],
    'd': ['a', 'c']
}
assert dfs_check(g5_true)

# a - b
# | \
# c   d
g6_true = {
    'a': ['b', 'c'],
    'b': ['a'],
    'c': ['a'],
    'd': ['a']
}
assert dfs_check(g6_true)

# a - b
# | \/
# c - d
g7_false = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'c'],
    'c': ['a', 'b', 'd'],
    'd': ['a', 'c']
}
assert not dfs_check(g7_false)
