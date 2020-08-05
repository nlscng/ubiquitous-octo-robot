from common.treenode.MyBST import IntNode


def flatten(root: IntNode) -> list:
    res = []

    def in_order(node: IntNode):
        if node is None:
            return
        in_order(node.left)
        res.append(node.val)
        in_order(node.right)

    in_order(root)
    return res


a = IntNode(4)
b = IntNode(2)
c = IntNode(6)
d = IntNode(1)
e = IntNode(3)
f = IntNode(5)
g = IntNode(7)

a.left = b
b.left = d
b.right = e
a.right = c
c.left = f
c.right = g

assert flatten(a) == [1, 2, 3, 4, 5, 6, 7], "Actual: {}".format(flatten(a))
