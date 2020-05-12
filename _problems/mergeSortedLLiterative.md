---
layout: page
title:  Merge Sorted Linked List (Iterative)
---




{% highlight python %}

class LinkedListNode:

    def __init__(self, val):

        self.val = val
        self.next = None



def mergeSortedLinkedList(l1, l2):

    dummy = ListNode(0)
    head = dummy
    while l1 and l2 : 
        if l1.val < l2.val : 
            dummy.next = l1
            l1 = l1.next
        else : 
            dummy.next = l2
            l2 = l2.next
        dummy = dummy.next

    if l1 : 
        dummy.next = l1
    elif l2 :
        dummy.next = l2
    return head.next


l1 = LinkedListNode(1)
l1.next = LinkedListNode(2)
l1.next.next = LinkedListNode(4)

l2 = LinkedListNode(1)
l2.next = LinkedListNode(3)
l2.next = LinkedListNode(4)

mergeSortedLinkedList()



{% endhighlight %}


