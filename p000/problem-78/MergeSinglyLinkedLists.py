# This problem was asked by Google.
#
# Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

'''
3 6, 9
2, 5, 8
1, 7

'''


from common.linked_list.MyLinkLlists import SinglyLinkedListNode as SLLN
import sys


def merge(roots: list) -> SLLN:
    # GG: tricky to get all corner cases right, especially handling multiple incoming LS, while creating one for result
    # O(m) in time, m being len of all incoming linked list combined, and same for space complexity, O(m)
    if not list:
        return None
    if len(roots) == 1:
        return roots[0]

    res_head = res_tail = None
    while len(roots) > 0:
        # find min out of current heads
        cur_min_node = None
        cur_min_idx = -1
        cur_min_val = sys.maxsize
        for idx, one_root in enumerate(roots):
            if one_root.value < cur_min_val:
                cur_min_node = one_root
                cur_min_val = cur_min_node.get_value()
                cur_min_idx = idx

        # remove current min heads from list of lists
        if cur_min_node.get_next() is None:
            roots.remove(cur_min_node)
        else:

            roots[cur_min_idx] = cur_min_node.get_next()
            cur_min_node.set_next(None)

        if res_head is None:
            res_tail = SLLN(cur_min_node.get_value())
            res_head = res_tail
        else:
            res_tail.set_next(SLLN(cur_min_node.get_value()))
            res_tail = res_tail.get_next()

    return res_head


assert merge([]) is None

n0 = SLLN(0)
n1 = SLLN(1)
n2 = SLLN(2)
n3 = SLLN(3)
n4 = SLLN(4)
n5 = SLLN(5)
n6 = SLLN(6)
n7 = SLLN(7)
n8 = SLLN(8)
n9 = SLLN(9)

# assert merge([n1]) == n1

list_238 = n2
n2.chain_next(n3).chain_next(n8)

list_147 = n1
n1.chain_next(n4).chain_next(n7)

list_0569 = n0
n0.chain_next(n5).chain_next(n6).chain_next(n9)

a = SLLN(0, SLLN(1, SLLN(2, SLLN(3, SLLN(4, SLLN(5, SLLN(6, SLLN(7, SLLN(8, SLLN(9))))))))))
assert merge([list_147, list_238, list_0569]) == a
