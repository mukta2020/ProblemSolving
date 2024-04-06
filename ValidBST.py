# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return (isBSTUtil(tree,float("-inf"), float("inf")))

def isBSTUtil(node, mini, maxi):
    if node is None:
        return True

    if node.value < mini or node.value > maxi:
        return False

    return (isBSTUtil(node.left, mini, node.value) and
            isBSTUtil(node.right, node.value, maxi))


root = BST(10)
root.left = BST(5)
root.right = BST(15)
root.left.right = BST(10)

if (validateBst(root)):
    print("valid BST")
else:
    print("Not a BST")