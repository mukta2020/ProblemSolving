# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    head1 = headOne
    head2 = headTwo
    tamp1 = tampHead = None
    front = False
    if head1.value < head2.value:
        tamp1 = LinkedList(head1.value)
        tamp1.next = head2
        tampHead = tamp1
        head1 = head1.next
        front = True
        head2 = tamp1
    while head1:
        found = False
        while head2.next:
            tamp1 = LinkedList(head1.value)
            if head2.next.value >= head1.value >= head2.value:
                tamp1.next = head2.next
                head2.next = tamp1
                found = True
                break
            head2 = head2.next
        if not found:
            head2.next = head1
            break
        head1 = head1.next
    return tampHead if front else headTwo



h1 = LinkedList(1)
second = LinkedList(2)
third = LinkedList(4)
four = LinkedList(5)

h1.next = second
second.next = third
third.next = four

h2 = LinkedList(3)

temp = mergeLinkedLists(h1, h2)
while(temp):
    print(temp.value)
    temp = temp.next