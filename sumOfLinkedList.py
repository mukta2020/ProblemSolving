# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    num1, num2 = "", ""
    while linkedListOne:
        num1 += str(linkedListOne.value)
        linkedListOne = linkedListOne.next

    while linkedListTwo:
        num2 += str(linkedListTwo.value)
        linkedListTwo = linkedListTwo.next

    num1 = int(num1[::-1])
    num2 = int(num2[::-1])
    sum = num1 + num2
    sum = str(sum)[::-1]
    print(sum)
    head = newLink = LinkedList(0)
    for s in sum:
        node = LinkedList(int(s))
        newLink.next = node
        newLink = node
    return head.next

fst = LinkedList(2)
second = LinkedList(4)
third = LinkedList(7)
last = LinkedList(1)

fst.next = second
second.next = third
third.next = last

four = LinkedList(9)
five = LinkedList(4)
six = LinkedList(5)

four.next = five
five.next = six

sumOfLinkedLists(fst, four)