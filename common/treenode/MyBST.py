class _MyBinaryTreeStem:
    def __init__(self, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.val = None

    def __str__(self):
        raise Exception('not implemented')

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def deepcopy(self):
        raise Exception('not implemented')


class MyBstNodeStringVal(_MyBinaryTreeStem):
    def __init__(self, val: str, left=None, right=None, parent=None):
        super().__init__(left, right, parent)
        self.val = val

    def __str__(self):
        """
        This is a pre-order to string method.
        :return:
        """
        res = self.val
        if self.left is not None:
            res = str(res) + ", " + str(self.left)
        if self.right is not None:
            res = str(res) + ", " + str(self.right)
        return res

    def __eq__(self, other):
        if other is None or not isinstance(other, MyBstNodeStringVal):
            return False
        return self.val == other.val and super().__eq__(other)

    def reset(self):
        self.left = self.right = self.parent = None

    def deepcopy(self):
        new_node = MyBstNodeStringVal(self.val)

        if self.left is not None:
            new_left = self.left.deepcopy()
            new_node.left = new_left
        if self.right is not None:
            new_right = self.right.deepcopy()
            new_node.right = new_right
        return new_node


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

a_copy = a.deepcopy()
assert a == a_copy


class MyBstNodeIntVal(_MyBinaryTreeStem):
    def __init__(self, val: int, left=None, right=None, parent=None):
        super().__init__(left, right, parent)
        self.val = val

    def __str__(self):
        res = self.val
        if self.left is not None:
            res = str(res) + ", " + str(self.left)
        if self.right is not None:
            res = str(res) + ", " + str(self.right)
        return str(res)

    def __eq__(self, other):
        if other is None or not isinstance(other, MyBstNodeIntVal):
            return False
        return self.val == other.val and super().__eq__(other)

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
