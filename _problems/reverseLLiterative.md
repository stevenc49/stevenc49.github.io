---
layout: page
title:  Reverse Linked List Iteratively
---




{% highlight python %}

class LinkedListNode:

    def __init__(self, val):

        self.val = val
        self.next = None



def reverse(head):

    curr = head
    prev = None
    next = None

    while curr:
        
        # save next node
        next = curr.next

        # reverse curr's pointer
        curr.next = prev

        # advance curr and prev
        prev = curr
        curr = next
    
    head = prev
    return head


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



{% endhighlight %}


