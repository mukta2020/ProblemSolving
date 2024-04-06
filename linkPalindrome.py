class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def linkedListPalindrome(head):
    temp = head
    res = []
    while (temp):
        res.append(temp.value)
        temp = temp.next
    return res == res[::-1]

root = LinkedList(0)
one = LinkedList(1)
two = LinkedList(2)
two2 = LinkedList(2)
one2 = LinkedList(1)
last = LinkedList(0)

root.next = one
one.next = two
two.next = two2
two2.next = one2
one2.next = last

print(linkedListPalindrome(root))