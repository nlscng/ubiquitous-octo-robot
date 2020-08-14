# This question was asked by Snapchat.
#
# Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere in the
# linked list, deep clone the list.


"""
A LL with a next and ALSO a RANDOM pointer?

if it's just the regular next pointer, this will be straight forward. I will need a set to track visited/cloned
nodes so we don't repeat.

The random basically splits the LL crawling. So recursivley, if the random walks onto an already-seen node,
we ignore and move on. Or if the head walks onto an already-seen node, the same.

with a LL of 1, 2, 3, 4, 5, 6
(node, next, random next)
1, 2, 5
2, 3, 1
3, 4, 6
4, 5, 3
5, 6, 4
6, none, 2

seen: {
1: 2
}
"""


# GG: very tricky mind blocker of pointer manipulation. I went down the route of recursion and that's harder to think
#  through 

class RandomLinkedListNode:
    def __init__(self, val: int, nxt=None, randomNxt=None):
        self.val = val
        self.next = nxt
        self.randomNext = randomNxt

    def __str__(self):
        out = str(self.val)
        if self.next:
            out = out + str(self.next)
        return out

    def __eq__(self, other):
        return other is not None and self.val == other.val

    def __hash__(self):
        return hash(self.val)


def random_linked_list_equal(a: RandomLinkedListNode, b: RandomLinkedListNode) -> bool:
    walker_a, walker_b = a, b
    while walker_a is not None or walker_b is not None:
        if walker_a is None or walker_b is None:
            return False
        if walker_a != walker_b:
            return False
        walker_a = walker_a.next
        walker_b = walker_b.next
    return True


def deep_clone_random_linked_list(root: RandomLinkedListNode):
    # this is O(n) in time, and O(n) in space, as we create a dict that scales with the size of the LL
    assert root is not None
    clones = dict()

    # populate the clones by walking through the LL, note the clones are not linked yet
    walker = root
    while walker is not None:
        clones[walker] = RandomLinkedListNode(walker.val)
        walker = walker.next

    # Walk through both the LL and clones, connecting the clones based on the original LL
    walker = root
    while walker is not None:
        clone = clones[walker]
        if walker.next is not None:
            clone.next = clones[walker.next]
        if clone.randomNext is not None:
            clone.randomNext = clones[walker.randomNext]
        walker = walker.next

    return clones[root]


# 1, 2, 5
# 2, 3, 1
# 3, 4, 6
# 4, 5, 3
# 5, 6, 4
# 6, none, 2
f = RandomLinkedListNode(6)
e = RandomLinkedListNode(5)
d = RandomLinkedListNode(4)
c = RandomLinkedListNode(3)
b = RandomLinkedListNode(2)
a = RandomLinkedListNode(1)
a.next = b
a.randomNext = e
b.next = c
b.randomNext = a
c.next = d
c.randomNext = f
d.next = e
d.randomNext = c
e.next = f
e.randomNext = d
f.next = None
f.randomNext = b

assert deep_clone_random_linked_list(a) == a

# 1, 2, 5
# 2, 3, 1
# 3, 4, 6
# 4, 5, 4
# 5, 6, 3
# 6, none, 2
f = RandomLinkedListNode(6)
e = RandomLinkedListNode(5)
d = RandomLinkedListNode(4)
c = RandomLinkedListNode(3)
b = RandomLinkedListNode(2)
a = RandomLinkedListNode(1)
a.next = b
a.randomNext = e
b.next = c
b.randomNext = a
c.next = d
c.randomNext = f
d.next = e
d.randomNext = f
e.next = f
e.randomNext = c
f.next = None
f.randomNext = b

assert deep_clone_random_linked_list(a) == a

# TBC: do the same thing in constant space
