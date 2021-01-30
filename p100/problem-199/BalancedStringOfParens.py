# This problem was asked by Facebook.
#
# Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of
# insertions and deletions. If there are multiple solutions, return any of them.
#
# For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".

##Facebook

"""
This at first looks like a dp problem, and almost a scary one. Like the ones
that allows you to add, delete or replace, like a word distance problem.

But this might be do able with scanning. As a usual balancing problem, a stack might
be useful, or at least the idea of it. But I will also need another counter for
the already-unbalanced right paren, if I am walking towards the right when scanning.

So to demonstrate:
(()
would result in the stack with one positive count, which means we have one left
over open left paren waiting to be closed, and nothing in the unbalanced counter.

)()
would start with a count of one in the unbalanced counter, and 0 in the stack
counter. Which means we need to balance from the left, either add one or remove
from left. Since the problem wants minimum insert and delete, both count counts
as one in terms of num of changes.

))()(

"""


def is_balanced(s: str) -> bool:
    assert s
    n = len(s)
    counter = 0
    for i in range(n):
        if s[i] == '(':
            counter += 1
        elif s[i] == ')':
            counter -= 1
        else:
            raise Exception(f'String s should contain only ( and ), but found {s[i]}')
    return counter == 0


def find_balanced_string(s: str) -> str:
    # This should be O(n) in both time and space
    assert s
    n = len(s)
    sw, fw = 0, 0  # slow walker, fast walker
    t = ''
    counter = 0  # balanced paren counter
    while fw < n:
        if s[fw] == ')':
            if counter <= 0:
                fw += 1
                sw = fw
            else:
                counter -= 1
                fw += 1
                if counter == 0:
                    t = t + s[sw:fw]
                    sw = fw
        elif s[fw] == '(':
            # reset counter back to 0 if it was smaller than 0 before.
            counter = max(counter, 0)
            counter += 1
            fw += 1

    if counter > 0:
        t = t + s[sw:fw] + "".join([')' for _ in range(counter)])

    return t


out = find_balanced_string('(()')
print(f'(() => {out}')
assert is_balanced(out)

out = find_balanced_string('))()(')
print(f'))()( => {out}')
assert is_balanced(out)

out = find_balanced_string(')(()())')
print(f')(()()) => {out}')
assert is_balanced(out)

out = find_balanced_string(')()))(())(()())()')
print(f')()))(())(()())() => {out}')
assert is_balanced(out)