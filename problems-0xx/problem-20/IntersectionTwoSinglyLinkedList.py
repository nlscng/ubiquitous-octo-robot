# This problem was asked by Google.
# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class LinkedListIntersectionNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node
        self.length = None

    def __str__(self):
        out = []
        node = self
        while node:
            out.append(str(node.val))
            node = node.next

        return ",".join(out)

    def get_length(self):
        if self.length is None:
            node = self
            len = 0
            while node:
                len += 1
                node = node.next

            self.length = len
        return self.length


test_linked_list = LinkedListIntersectionNode(1, LinkedListIntersectionNode(2, None))
assert str(test_linked_list) == "1,2"
assert test_linked_list.get_length() == 2


def find_intersection(a: LinkedListIntersectionNode, b: LinkedListIntersectionNode):
    """
    Given two singly linked list, a and b, find the intersection/merge element
    :param a:
    :param b:
    :return:
    """
    len_a = a.get_length()
    len_b = b.get_length()
    delta = abs(len_a - len_b)
    p = a
    q = b
    if len_a > len_b:
        for i in range(delta):
            p = p.next
    elif len_a < len_b:
        for i in range(delta):
            q = q.next

    merge_point = None
    while p and q:
        if p.val == q.val:
            merge_point = p.val
            break
        p = p.next
        q = q.next

    return merge_point


test_a = LinkedListIntersectionNode(1, LinkedListIntersectionNode(2, LinkedListIntersectionNode(3, LinkedListIntersectionNode(4, None))))
test_b = LinkedListIntersectionNode(1, LinkedListIntersectionNode(2, LinkedListIntersectionNode(3, LinkedListIntersectionNode(4, None))))
test_c = LinkedListIntersectionNode(5, LinkedListIntersectionNode(6, LinkedListIntersectionNode(3, LinkedListIntersectionNode(4, None))))
test_d = LinkedListIntersectionNode(5, LinkedListIntersectionNode(6, LinkedListIntersectionNode(7, LinkedListIntersectionNode(8, None))))
test_e = LinkedListIntersectionNode(3, LinkedListIntersectionNode(4))
test_f = LinkedListIntersectionNode(4)

assert find_intersection(test_a, test_b) == 1
assert find_intersection(test_a, test_c) == 3
assert find_intersection(test_a, test_d) is None
assert find_intersection(test_a, test_e) == 3
assert find_intersection(test_a, test_f) == 4

