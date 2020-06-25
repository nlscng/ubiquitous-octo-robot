from common.treenode.MyBST import BstIntNode


def flatten(root: BstIntNode) -> list:
    res = []

    def in_order(node: BstIntNode):
        if node is None:
            return
        in_order(node.left)
        res.append(node.val)
        in_order(node.right)

    in_order(root)
    return res


a = BstIntNode(4)
b = BstIntNode(2)
c = BstIntNode(6)
d = BstIntNode(1)
e = BstIntNode(3)
f = BstIntNode(5)
g = BstIntNode(7)

a.left = b
b.left = d
b.right = e
a.right = c
c.left = f
c.right = g

assert flatten(a) == [1, 2, 3, 4, 5, 6, 7], "Actual: {}".format(flatten(a))
