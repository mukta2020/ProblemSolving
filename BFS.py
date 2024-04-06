class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch2(self, array):
        queue = []
        if self.children is None:
            return
        queue.append(self)
        while len(queue) > 0:
            node = queue.pop(0)
            array.append(node.name)
            for c in node.children:
                queue.append(c)
        return array

    def breadthFirstSearch(self, array):
        queue = []
        if self is not None:
            queue.append(self)
        l = 0
        while l < len(queue):
            node = queue[l]
            array.append(node.name)
            if node.children is not None:
                for c in node.children:
                    queue.append(c)
                l += 1
        return array


root = Node("A")
root.addChild("B")
root.addChild("C")
root.addChild("D")
B = root.children[0]
B.addChild("E")
B.addChild("F")
D = root.children[2]
D.addChild("G")
D.addChild("H")
F = B.children[1]
F.addChild("I")
F.addChild("J")
G = D.children[0]
G.addChild("K")

print(root.breadthFirstSearch([]))


