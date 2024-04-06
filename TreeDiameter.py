# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def TreeHeight(tree):
    height, dia = 0, 0
    left_height, left_dia, right_height, right_dia = 0, 0, 0, 0
    longest_dia = 0
    if tree.left is not None:
       left_height, left_dia = TreeHeight(tree.left)
       height = left_height + 1
       longest_dia = height
    if tree.right is not None:
       right_height, right_dia = TreeHeight(tree.right)
       height = max(height, right_height + 1)
       longest_dia += right_height + 1

    dia = max(longest_dia, left_dia, right_dia)

    return height, dia


def binaryTreeDiameter(tree):
    return TreeHeight(tree)[1]

if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(3)
    root.right = BinaryTree(2)

    root.left.left = BinaryTree(7)
    root.left.right = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.left.left = BinaryTree(9)

    root.left.right.right = BinaryTree(5)
    root.left.right.right.right = BinaryTree(6)

    print(binaryTreeDiameter(root))