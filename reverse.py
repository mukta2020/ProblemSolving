# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None



def reverseLinkedList(head):
    prev, curr = None, head
    while curr:
        #curr.next, prev, curr = prev, curr, curr.next
        NextNode = curr.next
        curr.next = prev
        prev = curr
        curr = NextNode

    return prev



fst = LinkedList(1)
second = LinkedList(2)
third = LinkedList(3)
four = LinkedList(4)
five = LinkedList(5)

fst.next = second
second.next = third
third.next = four
four.next = five

temp = reverseLinkedList(fst)
while(temp):
    print(temp.value)
    temp = temp.next