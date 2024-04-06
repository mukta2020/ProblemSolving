# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
def shiftLinkedList(head, k):
    root = fst = head
    retHead = retRoot = None
    L, c = 1, 0
    while root.next:
        L += 1
        root = root.next
    if k == L:
        return head
    elif (k > L) or (k < 0 and k < -L):
        k = k % L
    elif -L <= k < 0:
        k = L + k
    if k == 0:
        return head
    while (head):
        c += 1
        if c == L - k:
            retHead = head.next
            head.next = None
            break
        else:
            head = head.next
    if retHead is not None:
        retRoot = retHead
        while retHead.next:
            retHead = retHead.next
        retHead.next = fst
    return retRoot

def shiftLinkedList1(head, k):
    fstHead = root = head
    sndHead = sndRoot = None
    c = 0
    while head.next:
        c += 1
        if c == k:
            sndHead = head.next
            break
        head = head.next
    if sndHead is not None:
        sndRoot = sndHead.next
        while (fstHead.next and sndHead.next):
            fstHead = fstHead.next
            sndHead = sndHead.next
        fstHead.next = None
        sndHead.next = root
    return sndRoot

fst = LinkedList(1)
second = LinkedList(2)
third = LinkedList(3)
four = LinkedList(4)
five = LinkedList(5)

fst.next = second
second.next = third
third.next = four
four.next = five
temp = shiftLinkedList(fst, -5)
while(temp):
    print(temp.value)
    temp = temp.next