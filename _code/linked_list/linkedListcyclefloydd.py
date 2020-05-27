

class LinkedListNode:

    def __init__(self, val):

        self.val = val
        self.next = None


def hasCycle(head):

    if not head:
        return False
    
    slow = head
    fast = head.next
    
    while True:

        # if either pointer is null, reached end of list and return False
        if slow is None or fast is None or fast.next is None:
            return False

        # cycle detected, exit and return True
        if slow is fast:
            return True 

        # advance pointers
        slow=slow.next
        fast=fast.next.next



    return False


head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next = head
# head.next.next = LinkedListNode(3)
# # head.next.next.next = head.next


print( hasCycle(head) )