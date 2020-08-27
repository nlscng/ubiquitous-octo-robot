# This problem was asked by Microsoft.
#
# Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes
# make up the number in reversed order.
#
# For example, the following linked list:
#
# 1 -> 2 -> 3 -> 4 -> 5
# is the number 54321.
#
# Given two linked lists in this format, return their sum in the same linked list format.
#
# For example, given
#
# 9 -> 9
# 5 -> 2
# return 124 (99 + 25) as:
#
# 4 -> 2 -> 1


"""
This is essentially the addition on paper itself. We add the lowest digits, carry over if any, and add the next lowest
digits.

So two walking pointer should work, after lining up since there might be difference is length

9, 9
5, 2

a: None
b: None
s: 1
c: 0
res: 4, 2
new: 1
"""

from common.linked_list.MyLinkLlists import SinglyLinkedListNode


def add_linked_list(a: SinglyLinkedListNode, b:SinglyLinkedListNode) -> SinglyLinkedListNode:
    walker_a, walker_b = a, b
    carry = 0
    res_walker = None
    res = None
    while walker_a is not None or walker_b is not None or carry == 1:
        # the math bits
        cur_sum = carry
        cur_sum += walker_a.value if walker_a is not None else 0
        cur_sum += walker_b.value if walker_b is not None else 0

        carry = 1 if cur_sum >= 10 else 0
        cur_sum = cur_sum - 10 if cur_sum >= 10 else cur_sum

        # the linked list bits
        new_node = SinglyLinkedListNode(cur_sum)
        if res is None:
            res_walker = new_node
            res = res_walker
        else:
            res_walker.next = new_node
            res_walker = new_node

        walker_a = walker_a.next if walker_a is not None else None
        walker_b = walker_b.next if walker_b is not None else None

    return res


a = SinglyLinkedListNode(9)
b = SinglyLinkedListNode(9)
c = SinglyLinkedListNode(5)
d = SinglyLinkedListNode(2)

a.next = b
c.next = d

e = SinglyLinkedListNode(4)
f = SinglyLinkedListNode(2)
g = SinglyLinkedListNode(1)
e.chain_next(f).chain_next(g)

assert add_linked_list(a, c) == e
