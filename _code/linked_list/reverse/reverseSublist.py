class LinkedListNode:

    def __init__(self, val):

        self.val = val
        self.next = None



def reverseBetween(head, m, n):

    prev = None
    curr = head

    # move prev and curr up to m
    while m>1:
        prev = curr
        curr = curr.next
        m-=1
        n-=1

    # connect beginning with reversed part
    connection = prev
    tail = curr

    while n>0:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        n-=1
    
    if connection:
        connection.next = prev
    else:
        head = prev

    tail.next = curr
    return head



head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)
head.next.next.next.next = LinkedListNode(5)

# print list
node = head
while node:
    print(node.val)
    node = node.next


head = reverseBetween(head, 2, 4)


# print list

print("\nresults:")
node = head
while node:
    print(node.val)
    node = node.next
