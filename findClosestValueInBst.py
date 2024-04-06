def findClosestValueInBst(tree, target):
    closet = float("inf")
    val = tree.value
    while tree != None:
        if target > tree.value:
            if closet > abs(target - tree.value):
                closet = abs(target - tree.value)
                val = tree.value
            tree = tree.right

        elif target < tree.value:
            if closet > abs(target - tree.value):
                closet = abs(target - tree.value)
                val = tree.value
            tree = tree.left
        else:
            return target
    return val

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = BST(10)
root.left = BST(8)
root.right = BST(12)
root.left.left = BST(2)
root.left.right = BST(4)
root.right.left = BST(11)
root.right.right = BST(15)

print(findClosestValueInBst(root, -100))