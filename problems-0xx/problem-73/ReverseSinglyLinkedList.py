# ood morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the head of a singly linked list, reverse it in-place.

from common.linked_list.MyLinkLlists import SinglyLinkedListNode


def reverse_singly_linked_list(head: SinglyLinkedListNode):
    if not head or head.next is None:
        return head

    walker = head
    next_walker = last_walker = None
    while walker.next is not None:
        next_walker = walker.next  # move walker to next node
        walker.next = last_walker
        last_walker = walker
        walker = next_walker

    walker.next = last_walker
    return walker


l_list = SinglyLinkedListNode(1, SinglyLinkedListNode(2, SinglyLinkedListNode(3)))
assert l_list.to_list()[::-1] == reverse_singly_linked_list(l_list).to_list()

