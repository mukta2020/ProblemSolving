# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeKthNodeFromEnd(head, k):
    root = retHead = head
    L, c = 0, 0
    while root:
        L += 1
        root = root.next
    if k == L:
        head.value = head.next.value
        head.next = head.next.next
        return head

    while (head):
        c += 1
        if c == L - k:
            if k == 1:
                head.next = None
            else:
                head.next = head.next.next
                break
        else:
            head = head.next
    return retHead


def removeKthNodeFromEnd1(head, k):
    fstHead = dummy = head
    sndHead = LinkedList(0)
    c = 0
    while head.next:
        c += 1
        if c == k:
            sndHead = head.next
            break
        head = head.next
    if k > c:
        dummy.value = dummy.next.value
        dummy.next = dummy.next.next
        return dummy
    while (fstHead.next and sndHead.next):
        fstHead = fstHead.next
        sndHead = sndHead.next
    fstHead.next = fstHead.next.next
    return dummy

fst = LinkedList(1)
second = LinkedList(2)
third = LinkedList(3)
four = LinkedList(4)
five = LinkedList(5)

fst.next = second
second.next = third
third.next = four
four.next = five
temp = removeKthNodeFromEnd1(fst, 5)
while(temp):
    print(temp.value)
    temp = temp.next