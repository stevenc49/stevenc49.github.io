class LinkedListNode:

    def __init__(self, val):

        self.val = val
        self.next = None


def palindromeLinkedList(head):

    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    print(slow)
    print(fast)

head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(2)
head.next.next.next = LinkedListNode(1)

palindromeLinkedList(head)