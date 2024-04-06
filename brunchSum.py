class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def branchSums(root):
    sum = []
    helperBrunchSum(root,0, sum)
    return sum

def helperBrunchSum(tree, currSum, sum):
    if tree is None:
        return
    currSum = currSum + tree.value
    if tree.left is None and tree.right is None:
        sum.append(currSum)
        return
    helperBrunchSum(tree.left, currSum, sum)
    helperBrunchSum(tree.right, currSum, sum)

root = BinaryTree(10)
root.left = BinaryTree(5)
root.right = BinaryTree(15)
root.left.right = BinaryTree(3)

print(branchSums(root))