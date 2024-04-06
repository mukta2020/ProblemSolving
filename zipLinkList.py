class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
def zipLinkedList1(linkedList):
    cur, pre = linkedList, None
    newLink = LinkedList(cur.value)
    retHead = newHead = newLink
    temp = None
    c = 0
    while cur is not None:
        cur.next, pre, cur = pre, cur, cur.next
        if cur is not None:
            temp = LinkedList(cur.value)
            newLink.next = temp
            newLink = temp
        c += 1
    count = c//2 + c%2
    while count > 0:
        p = pre.next
        if c % 2 == 0 and count == 1:
            pre.next = None
        else:
            pre.next = newHead.next
        l = newHead.next
        if c % 2 != 0 and count == 1:
            newHead.next = None
        else:
            newHead.next = pre
        pre = p
        newHead = l
        count -= 1

    return retHead

def zipLinkedList(linkedList):
    head1 = linkedList
    head2 = get2ndHalf(linkedList)
    reversehead2 = reverseLink(head2)
    return mergeLink(head1, reversehead2)

def get2ndHalf(linkedList):
    fastPointer = linkedList
    slowPointer = linkedList

    while fastPointer is not None and fastPointer.next is not None:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
    head2 = slowPointer.next
    slowPointer.next = None
    return head2

def mergeLink(head1, reversehead2):
    finalHead = head1
    while reversehead2:
        temp = head1.next
        head1.next = reversehead2
        head1 = head1.next

        tempreversehead2 = reversehead2.next

        head1.next = temp
        head1 = head1.next
        reversehead2 = tempreversehead2
    return finalHead

def reverseLink(head2):
    prev = None
    curr = head2
    while curr:
       # curr.next, prev, curr = prev, curr, curr.next

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

temp = zipLinkedList1(fst)
while(temp):
    print(temp.value)
    temp = temp.next