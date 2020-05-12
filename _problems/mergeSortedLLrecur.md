---
layout: page
title:  Merge Sorted Linked List (Recursive)
---




{% highlight python %}

class LinkedListNode:

    def __init__(self, val):

        self.val = val
        self.next = None


l1 = LinkedListNode(1)
l1.next = LinkedListNode(2)
l1.next.next = LinkedListNode(4)


l2 = LinkedListNode(2)
l2.next = LinkedListNode(3)
l2.next.next = LinkedListNode(4)



def mergeSortedLists(l1, l2):

    # if either list is empty, just return the other list
    # these are the base cases
    if not l1:
        return l2
        
    if not l2:
        return l1
    

    # recursively 
    if l1.val < l2.val:
        l1.next = mergeSortedLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeSortedLists(l2.next, l1)
        return l2

    



head = mergeSortedLists(l1, l2)

curr = head
while curr:
    print(curr.val)
    curr=curr.next




{% endhighlight %}


![image1](https://bubblesortblog.files.wordpress.com/2020/04/mergesortedlinkedlistsrecursive-1.jpg?w=768)
