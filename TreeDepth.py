
def nodeDepths(root, depth = 0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)

    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)

    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)

    print(nodeDepths(root))