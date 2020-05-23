class MyBstNode:
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
        if other is None or not isinstance(other, MyBstNode):
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right


a = MyBstNode('a')
b = MyBstNode('b')
c = MyBstNode('c')
d = MyBstNode('d')
a.left = b
a.right = c
# b.parent = a
# c.parent = a
b.left = d
# d.parent = b
assert str(a) == 'a, b, d, c'
