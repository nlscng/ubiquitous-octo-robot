# This problem was asked by Google.
#
# Given the head of a singly linked list, swap every two nodes and return its head.
#
# For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

"""
Things to ask, like if the list is guaranteed to be even in length. I am going to assume it is here.
I think we will need three utility pointers for a sequence of 4 nodes, a->b->c->d, swapping b and c:
1. one pointer to grab handle of a
2. one pointer to b,
3. one pointer to d
"""

from common.linked_list.MyLinkLlists import SinglyLinkedListNode as sll


def swap_every_two(node: sll) -> sll:
    assert node and node.next

    front = node
    back = node.next
    res = node.next
    head = None
    while front is not None:
        back = front.next
        tail = back.next

        if head is not None:
            head.set_next(back)
        front.set_next(tail)
        back.set_next(front)
        head = front
        front = tail

    return res


a = sll(0)
b = sll(1)
c = sll(2)
d = sll(3)
e = sll(4)
f = sll(5)
a.chain_next(b).chain_next(c).chain_next(d).chain_next(e).chain_next(f)

print(a)

A = sll(1)
B = sll(0)
C = sll(3)
D = sll(2)
E = sll(5)
F = sll(4)
A.chain_next(B).chain_next(C).chain_next(D).chain_next(E).chain_next(F)
print(A)
assert swap_every_two(a) == A, "Actual: {}".format(swap_every_two(a))
