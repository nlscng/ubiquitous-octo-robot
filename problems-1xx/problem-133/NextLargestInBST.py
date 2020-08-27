# Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.
#
# For example, the inorder successor of 22 is 30.
#
#    10
#   /  \
#  5    30
#      /  \
#    22    35
# You can assume each node has a parent pointer.


"""
O(n) solution would be to flatten the tree with in order traversal, turn it into a sorted list, then binary search for
it. The binary search is O(log n), but the traversal is O(n)

Better solution might be doing the binary search through the tree. I will have to keep a trailer pointer for the parent
of the target.

So a target is next largest to given node should have a few scenario, let's think this through:

left most child of immediate right child, or
first parent in parent hierarchy that's larger

Having parent pointer makes this easier, and doesn't impact performance on paper.

If there is no parent pointer though, have two walkers, one parent walker that's trailing by at least one node, keeping the value always
larger than target. The walker node will go down the tree and find the targt. When target is found, check if target
has right child. If no right child, then the trailing walker is our next largest. If there's a right child, ignore
the trailing walker, and search for left most child of this right child
"""

from common.treenode.MyBST import IntNode

# If there are no parent pointer, a trailing parent node that's kept bigger than k will help maintain the performance
# of this solution

def next_largest_node(root: IntNode, k: int) -> int:
    # this is O(log n) in time and O(1) in space
    assert root is not None

    walker = root
    while walker.val != k:
        if walker.val > k:
            try:
                walker = walker.left
            except ValueError:
                print("Value {} is not in this BST".format(k))
        if walker.val < k:
            try:
                walker = walker.right
            except ValueError:
                print("Value {} is not in this BST".format(k))

    # now target is found
    if walker.right is not None:
        # target has right branch, so next largest is the smallest in the right branch
        walker = walker.right
        while walker.left is not None:
            walker = walker.left
    else:
        # walker has no right child, so next largest is in the parents
        while walker.parent is not None:
            walker = walker.parent
            if walker.val > k:
                break

    return walker.val


#        10
#     /      \
#   5          30
#  / \         /  \
# 3   7       22    35

a = IntNode(10)
b = IntNode(5)
c = IntNode(30)
d = IntNode(3)
e = IntNode(7)
f = IntNode(22)
g = IntNode(35)
a.left = b
a.right = c
b.parent = a
c.parent = a
b.left = d
d.parent = b
b.right = e
e.parent = b
c.left = f
c.right = g
f.parent = c
g.parent = c

assert next_largest_node(a, 3) == 5
assert next_largest_node(a, 5) == 7
assert next_largest_node(a, 7) == 10
assert next_largest_node(a, 10) == 22
assert next_largest_node(a, 22) == 30
assert next_largest_node(a, 30) == 35
