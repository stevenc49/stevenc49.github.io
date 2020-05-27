

class LinkedListNode:

    def __init__(self, val):

        self.val = val
        self.next = None


def hasCycle(head):

    if not head:
        return False
    
    set = {}

    while head:

        if head in set:
            return True     # cycle detected
        else:
            set[head] = None    # add node to set

        # next node
        head = head.next

    # exited loop
    return False

    # map = {}
    # while head:

    #     if head.next and head.next.val not in map:
    #         map[head.val] = head.next.val
    #     else:

    #         if head.next == None:
    #             return False
    #         else:
    #             return True

    #     head = head.next
    
    # return False


head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
# head.next.next.next = head.next


print( hasCycle(head) )