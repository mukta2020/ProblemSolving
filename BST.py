
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Do not edit the return statement of this method.
        x = self
        y = None
        newnode = BST(value)
        while (x != None):
            y = x
            if (value < x.value):
                x = x.left
            else:
                x = x.right
        if (y == None):
            y = newnode
        elif (value < y.value):
            y.left = newnode
        else:
            y.right = newnode
        return y

    def contains(self, value):
        while self != None:
            if value > self.value:
                self = self.right
            elif value < self.value:
                self = self.left
            else:
                return True
        return False

    def remove(self, value, parent=None):
       curNode = self
       while curNode is not None:
           if value < curNode.value:
               parent = curNode
               curNode = curNode.left
           elif value > curNode.value:
               parent = curNode
               curNode = curNode.right
           else:
               if curNode.left is not None and curNode.right is not None:
                   curNode.value = curNode.right.getMinValue()
                   curNode.right.remove(curNode.value, curNode)
               elif parent is None:
                   if curNode.left is not None:
                       curNode.value = curNode.left.value
                       curNode.right = curNode.left.right
                       curNode.left = curNode.left.left
                   elif curNode.right is not None:
                       curNode.value = curNode.right.value
                       curNode.left = curNode.right.left
                       curNode.right = curNode.right.right
               elif parent.left == curNode:
                   parent.left = curNode.left if curNode.left is not None else curNode.right
               elif parent.right == curNode:
                   parent.right = curNode.left if curNode.left is not None else curNode.right
               break
       return self

    def getMinValue(self):
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr.value


def Inorder(root):
    if (root == None):
        return
    else:
        Inorder(root.left)
        print(root.value, end=" ")
        Inorder(root.right)

if __name__ == '__main__':
    root = BST(10)
    root.left = BST(8)
    root.right = BST(12)
    root.left.left = BST(2)
    root.left.right = BST(4)
    root.right.left = BST(11)
    root.right.right = BST(15)


    Inorder(root)
    print(root.contains(15))

    print("\nDelete 50")
    root = root.remove(50)
    print("Inorder traversal of the modified tree")
    Inorder(root)