# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def findLoop1(head):
    d = {}
    while head:
        if head not in d:
            d[head] = head.value
        else:
            return head
        head = head.next

def checkNextInVisitedNode(root, count, checkNode):
    while root and count != 0:
        if checkNode == root:
            return True
        root = root.next
        count = count - 1
    return False

def findLoop2(head):
    copy = head
    count = 0
    while head:
        count += 1
        if checkNextInVisitedNode(copy, count, head.next):
            return head.next
        head = head.next



fst = LinkedList(1)
second = LinkedList(2)
third = LinkedList(3)
four = LinkedList(4)
five = LinkedList(5)

fst.next = second
second.next = third
third.next = four
four.next = five
five.next = fst

temp = findLoop1(fst)
while(temp):
    print(temp.value)
    temp = temp.next