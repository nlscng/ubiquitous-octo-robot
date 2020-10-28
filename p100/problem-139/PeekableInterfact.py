# Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface, which also
# implements peek(). peek shows the next element that would be returned on next().
#
# Here is the interface:
# class PeekableInterface(object):
#     def __init__(self, iterator):
#         pass
#
#     def peek(self):
#         pass
#
#     def next(self):
#         pass
#
#     def hasNext(self):
#         pass


class PeekableInterface(object):
    def __init__(self, iterator):
        assert iterator is not None
        self.iterator = iterator
        self.my_next = self.iterator.next() if self.hasNext() else None

    def peek(self):
        return self.my_next

    def next(self):
        res = self.my_next
        self.my_next = self.iterator.next() if self.hasNext() else None
        return res

    def hasNext(self):
        return self.my_next is not None


