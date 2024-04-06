# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if node.right is not None:
        return left_most_node(node.right)
    else:
        return first_unvisited_parent(node)

def first_unvisited_parent(node):
    parent = node.parent
    child = node
    while parent is not None and child == parent.right:
        child = parent
        parent = child.parent
    return parent.value

def left_most_node(node):
    left_most = node
    while left_most.left is not None:
        left_most = left_most.left
    return left_most.value

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


print(findSuccessor(root, six))
