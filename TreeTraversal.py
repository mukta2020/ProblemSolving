class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

def inOrderTraverse(tree, array):
    if tree:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array

def preOrderTraverse(tree, array):
    if tree:
        #print(tree.val, end=" ")
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

def postOrderTraverse(tree, array):
    if tree:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array

def PostOrderTraversalRecursive(root):
    res = []
    if root:
        res = res + PostOrderTraversalRecursive(root.left)
        res = res + PostOrderTraversalRecursive(root.right)
        res.append(root.val)
    return res
def PreorderTraversalRecursive(root):
    res = []
    if root:
        res.append(root.val)
        res = res + PreorderTraversalRecursive(root.left)
        res = res + PreorderTraversalRecursive(root.right)
    return res
def InOrderTraversalRecursive(root):
    res = []
    if root:
        res = res + InOrderTraversalRecursive(root.left)
        res.append(root.val)
        res = res + InOrderTraversalRecursive(root.right)
    return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("post order traversal of binary tree is")
print(postOrderTraverse(root, []))
print("\n......pre order traversal............\n")
print(PreorderTraversalRecursive(root))
print("\n......in order traversal........\n")
print(inOrderTraverse(root, []))