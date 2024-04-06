class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def buildingList(node, copy , nHead):
    if node is None:
        node = copy
        nHead = node
    else:
        node.next = copy
        node = node.next
    return node, nHead
def rearrangeLinkedList(head, k):
    k1 = kNode = s1 = sNode = g1 = gNode = None
    copy = head
    while copy:
        if copy.value == k:
           kNode, k1 = buildingList(kNode, copy, k1)
        elif copy.value < k:
            sNode, s1 = buildingList(sNode, copy, s1)
        elif copy.value >= k:
            gNode, g1 = buildingList(gNode, copy, g1)
        copy = copy.next

    if kNode is not None and sNode is not None:
        sNode.next = k1
    elif kNode is None and sNode is not None and gNode is not None:
        sNode.next = g1

    if gNode is not None:
        if kNode is not None:
            kNode.next = g1
        if gNode.next is not None:
            gNode.next = None
    if sNode is not None:
        return s1
    elif kNode is not None:
        return k1
    else:
        return g1

fst = LinkedList(6)
second = LinkedList(0)
third = LinkedList(5)
four = LinkedList(2)
five = LinkedList(1)
six = LinkedList(4)

fst.next = second
second.next = third
third.next = four
four.next = five
five.next = six

temp = rearrangeLinkedList(fst,3)
while(temp):
    print(temp.value)
    temp = temp.next