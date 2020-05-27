class LinkedListNode:

    def __init__(self, val):

        self.val = val
        self.next = None


def reverse(head):

    if not head:
        return
    
    head.next = reverse(head)


head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)

# print list
node = head
while node:
    print(node.val)
    node = node.next


head = reverse(head)


# print list
node = head
while node:
    print(node.val)
    node = node.next