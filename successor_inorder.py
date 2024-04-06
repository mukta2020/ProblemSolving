class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def inOrderTraverse(tree, array):
    if tree:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array

def findSuccessor(tree, node):
    inorderArray = inOrderTraverse(tree, [])

    for i, n in enumerate(inorderArray):
        if n != node:
            continue
        if i == len(inorderArray) - 1:
            return None
        return inorderArray[i + 1]


root = BinaryTree(5)
three = BinaryTree(3)
six = BinaryTree(6)
two = BinaryTree(2)
one = BinaryTree(1)
ten = BinaryTree(10)
nine = BinaryTree(9)
twelve = BinaryTree(12)
four = BinaryTree(4)
zero = BinaryTree(0)

three.parent = root
ten.parent = root
two.parent = three
one.parent = two
six.parent = three
ten.parent = root
nine.parent = ten
twelve.parent = ten
four.parent = twelve
zero.parent = twelve

root.left = three
root.right = ten
root.left.left = two
root.left.right = six

root.left.left.left = one
root.right.left = nine
root.right.right = twelve
root.right.right.left = four
root.right.right.right = zero

print(findSuccessor(root, 5))