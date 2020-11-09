# This problem was asked by Airbnb.
#
# Given a linked list and a positive integer k, rotate the list to the right by k places.
#
# For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.
#
# Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.

"""

"""

from common.linked_list.MyLinkLlists import SinglyLinkedListNode as SLL

def rotate_linked_list(root: SLL, n: int) -> SLL:
    # this should be O(n) in time and O(1) in space
    assert root and n >= 0

    head = tail = root

    while tail.next:
        tail = tail.next

    for i in range(n):
        tail.next = head
        head = head.next
        tail = tail.next

    tail.next = None

    return head


test1 = SLL(7)
test1.chain_next(SLL(7)).chain_next(SLL(3)).chain_next(SLL(5))
out1 = SLL(3)
out1.chain_next(SLL(5)).chain_next(SLL(7)).chain_next(SLL(7))
assert rotate_linked_list(test1, 2) == out1


test2 = SLL(1)
test2.chain_next(SLL(2)).chain_next(SLL(3)).chain_next(SLL(4)).chain_next(SLL(5))
out2 = SLL(4)
out2.chain_next(SLL(5)).chain_next(SLL(1)).chain_next(SLL(2)).chain_next(SLL(3))
assert rotate_linked_list(test2, 3) == out2
