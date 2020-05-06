# ood morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the head of a singly linked list, reverse it in-place.

class SingleLinkedListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def set_next(self, next):
        self.next = next
        return self

    def set_value(self, value):
        self.value = value
        return self

    def to_list(self, accu:list=None):
        if accu is None:
            res = [self.value]
        else:
            res = accu
            res.append(self.value)
        if self.next is not None:
            self.next.to_list(res)
        return res

    def __str__(self):
        return str(self.value) + str(self.next) if self.next is not None else str(self.value)


def reverse_singly_linked_list(head: SingleLinkedListNode):
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


l_list = SingleLinkedListNode(1, SingleLinkedListNode(2, SingleLinkedListNode(3)))
assert l_list.to_list()[::-1] == reverse_singly_linked_list(l_list).to_list()

