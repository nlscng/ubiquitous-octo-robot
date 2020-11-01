# This problem was asked by Google.
#
# Given a linked list, sort it in O(n log n) time and constant space.
#
# For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.

"""
This seems like a quick sort or merge sort, in place, with a linked list.

If I can merge two sorted linked list in place (aka with constant space), I can merge sort this.

"""

from common.linked_list.MyLinkLlists import SinglyLinkedListNode as SLLN


def merge_two_sorted(a: SLLN, b: SLLN) -> SLLN:
    assert a and b
    head: SLLN = SLLN()
    p: SLLN = head
    ap: SLLN = a
    bp: SLLN = b
    while ap or bp:
        if ap and bp:
            if ap.value <= bp.value:
                t = ap
                ap = ap.next
                p.next = t
                p = p.next
                p.next = None
            else:
                t = bp
                bp = bp.next
                p.next = t
                p = p.next
                p.next = None
        elif ap:
            p.next = ap
            break
        else:
            p.next = bp
            break
    head = head.next
    return head


a = SLLN(1)
b = SLLN(2)
c = SLLN(3)
d = SLLN(4)
e = SLLN(5)
f = SLLN(6)

a.next = c
c.next = d
b.next = e
e.next = f
# print(merge_two_sorted(a, b))


def merge_sort(lis: SLLN) -> SLLN:
    assert lis

    if lis.next is None:
        return lis

    # find mid
    sp, fp = lis, lis.next
    while fp and fp.next:
        sp = sp.next
        fp = fp.next
        if fp:
            fp = fp.next

    right = sp.next
    sp.next = None
    right = merge_sort(right)
    left = merge_sort(lis)
    lis = merge_two_sorted(left, right)
    return lis


# 3,5,6,4,1,2
c.next = e
e.next = f
f.next = d
d.next = a
a.next = b
b.next = None
print(merge_sort(c))

