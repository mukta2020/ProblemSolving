# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList.next
    prev = linkedList

    while current != None:
        if current.value == prev.value:
            prev.next = current.next
            current = current.next
        else:
            current = current.next
            prev = prev.next
    return linkedList

fst = LinkedList(1)
second = LinkedList(1)
third = LinkedList(2)
four = LinkedList(3)
five = LinkedList(3)
six = LinkedList(3)

fst.next = second
second.next = third
third.next = four
four.next = five
five.next = six

temp = removeDuplicatesFromLinkedList(fst)
while(temp):
    print(temp.value)
    temp = temp.next
