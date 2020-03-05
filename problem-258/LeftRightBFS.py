# In Ancient Greece, it was common to write text with the first line going left to right, the second line going right
# to left, and continuing to go back and forth. This style was called "boustrophedon".
#
# Given a binary tree, write an algorithm to print the nodes in boustrophedon order.
#
# For example, given the following tree:
#
#        1
#     /     \
#   2         3
#  / \       / \
# 4   5     6   7
# You should return [1, 3, 2, 4, 5, 6, 7].

from collections import deque


class LRBFS:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(node: LRBFS):
    out = bfs_helper(node)
    return out


def bfs_helper(node: LRBFS):
    if not node:
        return []
    buff = deque()
    buff.append(node)
    out = []

    while len(buff) > 0:
        nxt = buff.popleft()
        if nxt is not None:
            out.append(nxt.val)
            buff.append(nxt.left)
            buff.append(nxt.right)
        else:
            break

    return out


test_a = LRBFS(0, LRBFS(1, LRBFS(3), LRBFS(4)), LRBFS(2, LRBFS(5), LRBFS(6)))
assert bfs(None) == []
assert ",".join([str(x) for x in bfs(test_a)]) == "0,1,2,3,4,5,6"


def left_right_bfs(node: LRBFS):
    # this is the alternativing bfs, see helper
    out = lrbfs_helper(node)
    return out


def lrbfs_helper(node: LRBFS):
    # this helper uses two stacks, one for levels going right, the other going left; dupe code should be refactored
    if node is None or type(node) is not LRBFS:
        return []

    out = []
    reverse = False
    left_stack = []
    right_stack = []
    left_stack.append((node, 0))
    while left_stack or right_stack:
        if left_stack:
            while left_stack:
                nxt = left_stack.pop()
                if nxt[0] is not None:
                    out.append(nxt[0].val)
                    level = nxt[1]
                    right_stack.append((nxt[0].left, level + 1))
                    right_stack.append((nxt[0].right, level + 1))
        elif right_stack:
            while right_stack:
                nxt = right_stack.pop()
                if nxt[0] is not None:
                    out.append(nxt[0].val)
                    level = nxt[1]
                    left_stack.append((nxt[0].right, level + 1))
                    left_stack.append((nxt[0].left, level + 1))

    return out


assert left_right_bfs(None) == []
assert ",".join([str(x) for x in left_right_bfs(test_a)]) == "0,2,1,3,4,5,6"
