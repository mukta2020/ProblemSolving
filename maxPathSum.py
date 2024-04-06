class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxPathSumHelper(tree):
    left_value, right_value = 0, 0
    max2_left, max2_right = 0, 0
    root_value, max_value, max2 = 0, 0, 0
    longest_path = 0
    if tree.left is not None:
       left_value, max2_left = maxPathSumHelper(tree.left)
    if tree.right is not None:
       right_value, max2_right = maxPathSumHelper(tree.right)

    if left_value > right_value:
        max_value = left_value
        max2 = right_value
    else:
        max_value = right_value
        max2 = left_value
    root_value = max(max_value + tree.value, tree.value)
    return root_value, max2

def maxPathSum(tree):
    a, b = maxPathSumHelper(tree)
    return max(a + b, a, b)

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
print(maxPathSum(root))