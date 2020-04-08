# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be
# smaller than the length of the list.
#
# The list is very long, so making more than one pass is prohibitively expensive.
#
# Do this in constant space and in one pass.

class SinglyLinkedListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

    def __str__(self):
        if self.next_node is None:
            return "{}".format(str(self.val))
        else:
            my_val = self.val
            return str(self.val) + ', ' + str(self.next_node)

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node


def remove_kth_last(sl: SinglyLinkedListNode, k: int):
    '''
    Given a singly linked list, remove the kth to last element from it, with constant space and one pass
    :param sl:
    :return:
    '''
    if not isinstance(sl, SinglyLinkedListNode):
        raise Exception("Expected a SinglyLinkedListNode, got {} instead.".format(type(sl)))

    length = 0
    walker = sl
    while walker is not None:
        walker = walker.get_next_node()
        length += 1

    assert length >= k, "Size of the linked list needs to be at least k; found size: {}".format(length)

    first_walker = sl
    i = 0
    # fast forward by k step first
    while i < k:
        first_walker = first_walker.get_next_node()
        i += 1

    second_walker = sl
    parent_to_second_walker = None
    while first_walker is not None:
        first_walker = first_walker.get_next_node()
        parent_to_second_walker = second_walker
        second_walker = second_walker.get_next_node()

    # found the kth last element, time to remove it
    if second_walker == sl:
        return second_walker.get_next_node()
    else:
        parent_to_second_walker.set_next_node(second_walker.next_node)
        return sl


a = SinglyLinkedListNode('a')
b = SinglyLinkedListNode('b')
c = SinglyLinkedListNode('c')
d = SinglyLinkedListNode('d')
e = SinglyLinkedListNode('e')

a.set_next_node(b)
assert str(a) == "a, b"
b.set_next_node(c)
assert str(a) == 'a, b, c'

assert str(remove_kth_last(a, 1)) == 'a, b', "Actual output: {}".format(str(remove_kth_last(a, 1)))
b.set_next_node(c)

assert str(a) == "a, b, c"
assert str(remove_kth_last(a, 3)) == "b, c"

a.set_next_node(b)
assert str(remove_kth_last(a, 2)) == "a, c"
