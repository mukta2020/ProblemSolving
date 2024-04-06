# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxPathSumHelper(tree):
    value, path = 0, 0
    left_val, right_val = 0, 0
    left_path, right_path = float("-inf"), float("-inf")
    root_path, longest_path = float("-inf"), float("-inf")
    if tree.left is None and tree.right is None:
        return tree.value, tree.value
    if tree.left is not None:
       left_val, path = maxPathSumHelper(tree.left)
       left_path = left_val + tree.value
       root_path = left_val
    if tree.right is not None:
       right_val, path = maxPathSumHelper(tree.right)
       value = max(left_val, right_val)
       right_path = value + tree.value
       root_path += right_val + tree.value

    longest_path = max(longest_path, path)
    path = max(root_path, left_path, right_path, longest_path)
    return max(right_path, left_path), path

def maxPathSum(tree):
    return maxPathSumHelper(tree)[1]

if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    print(maxPathSum(root))