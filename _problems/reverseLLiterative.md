---
layout: page
title:  Reverse Linked List Iteratively
last_solved: 2020-06-06
category: linked list
leetcode_url: https://leetcode.com/problems/reverse-linked-list/
status: Solved
---




{% highlight python %}

def reverseList(self, head: ListNode) -> ListNode:
    
    prev = None
    curr = head
    next = None
    
    while curr:
        
        next = curr.next    # save next
        
        curr.next = prev    # do reversal
        
        prev = curr
        curr = next
    
    return prev


{% endhighlight %}


