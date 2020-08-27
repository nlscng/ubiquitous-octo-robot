# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For
# example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
#
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
#
# Implement car and cdr.

def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(func):
    return func(lambda x, y: x)


def cdr(func):
    return func(lambda x, y: y)


a = 42
b = 24
assert car(cons(a, b)) == a
assert cdr(cons(a, b)) == b
