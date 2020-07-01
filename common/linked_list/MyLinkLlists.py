class SinglyLinkedListNode:
    def __init__(self, value=None, nxt=None):
        self.value = value
        self.next = nxt

    def set_next(self, next_node):
        self.next = next_node
        return self

    def chain_set_next(self, next_node):
        self.next = next_node
        return next_node

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value
        return self

    def get_value(self):
        return self.value

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

    def __eq__(self, other):
        if other is None or not isinstance(other, SinglyLinkedListNode):
            return False

        if self.value != other.get_value():
            return False

        return self.next == other.get_next()


n0 = SinglyLinkedListNode(0)
n1 = SinglyLinkedListNode(1)
n2 = SinglyLinkedListNode(2)

a0 = SinglyLinkedListNode(0)
a1 = SinglyLinkedListNode(1)
a2 = SinglyLinkedListNode(2)
assert n0 == n0
assert n0 != n1

n0.chain_set_next(n1).chain_set_next(n2)
a0.chain_set_next(a1).chain_set_next(a2)
assert n0 == a0

a1.set_value(42)
assert n0 != a0
