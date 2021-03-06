
"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and
deserialize(s), which deserializes the string back into the tree.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    val_list = traverse(root, [])
    return ",".join(val_list)

def traverse(my_node, acc = []):
    if my_node.left is not None:
        acc = traverse(my_node.left, acc)

    acc.append(str(my_node.val))

    if my_node.right is not None:
        acc = traverse(my_node.right, acc)

    return acc



def deserialize(str):
    if not str:
        return None
    else:
        return None



node = Node('root', Node('left', Node('left.left')), Node('right'))
assert serialize(node) == "left.left,left,root,right"

# assert deserialize(serialize(node)).left.left.val == 'left.left'
