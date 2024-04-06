def inorderLeftPush(nodeStack, node):
    while (node):
        nodeStack.append(node)
        node = node.left

def iterativeInorder(root):
    if root is None:
        return
    nodeStack = []
    nodes = []
    inorderLeftPush(nodeStack, root)

    while(len(nodeStack) > 0):
        popNode = nodeStack.pop()
        #print(popNode.data)
        nodes.append(popNode.data)
        if popNode.right:
            newNode = popNode.right
            inorderLeftPush(nodeStack, newNode)
    return nodes

#def iterativeInOrderTraversal(tree, callback):