class LinkedListNode:

    def __init__(self, val):

        self.val = val
        self.next = None


l1 = LinkedListNode(1)
l1.next = LinkedListNode(2)
l1.next.next = LinkedListNode(4)


l2 = LinkedListNode(1)
l2.next = LinkedListNode(3)
l2.next.next = LinkedListNode(4)



def mergeSortedLists(l1, l2):

    dummy = LinkedListNode(0)
    curr = dummy

    while l1 and l2:

        if l1.val <= l2.val:
            curr.next = l1
            curr = l1
            l1 = l1.next
        else:
            curr.next = l2
            curr = l2
            l2 = l2.next

    while l1:
        curr.next = l1
        curr = l1
        l1 = l1.next

    while l2:
        curr.next = l2
        curr = l2
        l2 = l2.next

    return dummy.next

head = mergeSortedLists(l1, l2)

curr = head
while curr:
    print(curr.val)
    curr=curr.next
