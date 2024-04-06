def invertBinaryTree(tree):
    leftTree = None
    if tree is None:
        return
    leftTree = tree.left
    tree.left = tree.right
    tree.right = leftTree

    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)

    r = invertBinaryTree(root)
    print(r)