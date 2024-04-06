class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    def getChild(self):
        return self.children

    def depthFirstSearch(self, array):
        children = self.getChild()
        if children is None:
            return
        array.append(self.name)
        for c in children:
            c.depthFirstSearch(array)
        return array

    def depthFirstSearch1(self, array):
        stack = []
        if self is not None:
            stack.append(self)
        while len(stack) > 0:
            p = stack.pop()
            array.append(p.name)
            children = p.getChild()
            if children is not None:
                for c in children[::-1]:
                    stack.append(c)
        return array


root = Node("A")
root.addChild("B")
root.addChild("C")
root.addChild("D")
B = root.children[0]
B.addChild("E")
B.addChild("F")

print(root.depthFirstSearch([]))


