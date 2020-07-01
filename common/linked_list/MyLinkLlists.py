class SinglyLinkedListNode:
    def __init__(self, value=None, nxt=None):
        self.value = value
        self.next = nxt

    def set_next(self, nxt):
        self.next = nxt
        return self

    def set_value(self, value):
        self.value = value
        return self

    def to_list(self, accu: list = None):
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
