# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example 1:

# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:

# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

from collections import deque

class LinkedListNode:

    def __init__(self, val):

        self.val = val
        self.next = None



def reorderList(head):

        # push all into list
        q = deque()
        while head:
            q.append(head)
            head = head.next
        
        
        dummy = LinkedListNode(0)
        cur = dummy
        even = False
        
        while q:
            
            node = q.pop() if even else q.popleft()
            node.next = None
            
            cur.next = node
            cur = cur.next
            
            even ^= True
        
        return dummy.next


# create sample linked list
head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)
head.next.next.next.next = LinkedListNode(5)

# run the code
head = reorderList(head)


while head:
    print(head.val)
    head=head.next



