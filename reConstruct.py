class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    tree = BST(preOrderTraversalValues[0])
    for i in range(1, len(preOrderTraversalValues)):
        insert(tree, preOrderTraversalValues[i])
    return tree

def insert(node, value):
    if node is None:
        return BST(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

print(reconstructBst([10,4,2,1,5,17,19,18]))