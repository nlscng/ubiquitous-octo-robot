# This problem was asked by Google.
#
# Determine whether a doubly linked list is a palindrome. What if it’s singly linked?
#
# For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.


'''
1,4,3,4,1 -> true

I can grab head, and tail if not given, then move two of them towards the center while checking
this is O(2n) in time, once to find tail, once to check

singly linked:

I can use two pointers, one moves twice as fast maybe? I need to handle even and odd size list. I can put everything
found by the slow ptr into a stack, and when end is found, start moving the slow ptr again and pop the stack while
checking

 1,4,3,4,1
     s
           f
  1,4,4,1
    s
        f


1331
 s
   f
'''

from common.linked_list.MyLinkLlists import SinglyLinkedListNode


def is_linked_list_palindrome(l_list: SinglyLinkedListNode) -> bool:
    if not list:
        return False
    if l_list.next is None:
        return True

    s_walker, f_walker = l_list, l_list.get_next()
    stack = []

    while f_walker is not None and f_walker.get_next() is not None:
        stack.append(s_walker)
        s_walker = s_walker.get_next()
        f_walker = f_walker.get_next().get_next()
    stack.append(s_walker)

    # by this time we should be at mid point
    if len(stack) % 2 == 1:
        # stack size is odd
        stack.pop()

    while s_walker.get_next() is not None:
        past = stack.pop()
        s_walker = s_walker.get_next()
        if past.get_value() != s_walker.get_value():
            return False
    return True


a = SinglyLinkedListNode(1)
b = SinglyLinkedListNode(3)
c = SinglyLinkedListNode(3)
d = SinglyLinkedListNode(1)

assert is_linked_list_palindrome(a)

a.chain_next(b).chain_next(c).chain_next(d)
assert is_linked_list_palindrome(a)

e = SinglyLinkedListNode(1)
d.set_value(3)
d.set_next(e)
assert is_linked_list_palindrome(a)
