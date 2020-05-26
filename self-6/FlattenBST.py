from common.treenode.MyBST import MyBstNodeIntVal

def flatten(root: MyBstNodeIntVal) -> list:
    res = []
    def in_order(node: MyBstNodeIntVal):
        if node is None:
            return
        in_order(node.left)
        res.append(node.val)
        in_order(node.right)

    in_order(root)
    return res

a = MyBstNodeIntVal(4)
b = MyBstNodeIntVal(2)
c = MyBstNodeIntVal(6)
d = MyBstNodeIntVal(1)
e = MyBstNodeIntVal(3)
f = MyBstNodeIntVal(5)
g = MyBstNodeIntVal(7)

a.left = b
b.left = d
b.right = e
a.right = c
c.left = f
c.right = g

assert flatten(a) == [1,2,3,4,5,6,7], "Actual: {}".format(flatten(a))
