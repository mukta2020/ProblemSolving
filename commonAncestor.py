class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDepth(topAncestor, descendantOne)
    depthTwo = getDepth(topAncestor, descendantTwo)
    if depthTwo > depthOne:
        return TraverseGraph(descendantTwo, descendantOne, depthTwo, depthOne)
    else:
        return TraverseGraph(descendantOne, descendantTwo, depthOne, depthTwo)

def TraverseGraph(descendantlow, descendantHigh, depthlow, depthHigh):
    while depthlow > depthHigh:
        descendantlow = descendantlow.ancestor
        depthlow -= 1
    if descendantlow == descendantHigh:
        return descendantlow

    while descendantlow.ancestor != descendantHigh.ancestor:
        descendantlow = descendantlow.ancestor
        descendantHigh = descendantHigh.ancestor
    return descendantlow.ancestor if descendantlow.ancestor is not None else descendantlow

def getDepth(topAncestor, descendant):
    d = 0
    while descendant is not topAncestor:
        descendant = descendant.ancestor
        d += 1
    return d

A = AncestralTree("A")
B = AncestralTree("B")
C = AncestralTree("C")
D = AncestralTree("D")
E = AncestralTree("E")
F = AncestralTree("F")
G = AncestralTree("G")
H = AncestralTree("H")
I = AncestralTree("I")
B.ancestor = A
C.ancestor = A
D.ancestor = B
E.ancestor = B
F.ancestor = C
G.ancestor = C
I.ancestor = D
H.ancestor = D
print(getYoungestCommonAncestor(A,H, I))