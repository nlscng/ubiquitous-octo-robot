# An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev
# fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR
# linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at
# index.
#
# If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and
# dereference_pointer functions that converts between nodes and memory addresses.

##Google

def get_pointer(object):
    return 1234


def dereference_pointer(address):
    return 4321


class XorLinkedListNode:
    # I guess this xor linked list rely on the special fact
    # that A xor B = C => A xor C = B, B xor C = A
    def __init__(self, value: int, prev_add):
        self.value = value
        self.ptr = prev_add ^ 0

    def set_pointer(self, new_ptr):
        self.ptr = new_ptr


class XorLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        if self.head is None:
            self.head = XorLinkedListNode(value, 0)
        else:
            node = self.head
            prev_add = 0
            while node.ptr is not None:
                cur_add = get_pointer(node)
                node = dereference_pointer(prev_add ^ node.ptr)
                prev_add = cur_add

            new_node = XorLinkedListNode(value, get_pointer(node))
            node.set_ptr(prev_add ^ get_pointer(new_node))

    def get(self, index):
        if index <= 0:
            return None

        node = self.head
        prev_add = 0
        while node.ptr is not None and index > 0:
            cur_add = get_pointer(node)
            node = dereference_pointer(prev_add ^ cur_add)
            prev_add = cur_add
            index -= 1
        return node.value

# hmm, how do I test this with the fake get_pointer and dereference ...
