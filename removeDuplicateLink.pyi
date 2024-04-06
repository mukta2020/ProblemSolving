# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    head = linkedList
    while linkedList:
        if linkedList.next is not None and linkedList.value == linkedList.next.value:
            linkedList = linkedList.next.next
        else:
            linkedList = linkedList.next
    return head

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
