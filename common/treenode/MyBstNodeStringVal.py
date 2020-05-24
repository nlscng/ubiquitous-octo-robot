class MyBstNodeStringVal:
    def __init__(self, val: str, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        res = self.val
        if self.left is not None:
            res = res + ", " + str(self.left)
        if self.right is not None:
            res = res + ", " + str(self.right)
        return res

    def __eq__(self, other):
        if other is None or not isinstance(other, MyBstNodeStringVal):
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right

    def reset(self):
        self.left = self.right = self.parent = None


a = MyBstNodeStringVal('a')
b = MyBstNodeStringVal('b')
c = MyBstNodeStringVal('c')
d = MyBstNodeStringVal('d')
a.left = b
a.right = c
# b.parent = a
# c.parent = a
b.left = d
# d.parent = b
assert str(a) == 'a, b, d, c'


class MyBstNodeIntVal:
    def __init__(self, val: int, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        res = self.val
        if self.left is not None:
            res = str(res) + ", " + str(self.left)
        if self.right is not None:
            res = str(res) + ", " + str(self.right)
        return str(res)

    def __eq__(self, other):
        if other is None or not isinstance(other, MyBstNodeStringVal):
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right

    def reset(self):
        self.left = self.right = self.parent = None


a = MyBstNodeIntVal(1)
b = MyBstNodeIntVal(2)
c = MyBstNodeIntVal(3)
d = MyBstNodeIntVal(4)
a.left = b
a.right = c
# b.parent = a
# c.parent = a
b.left = d
# d.parent = b
assert str(a) == '1, 2, 4, 3'
