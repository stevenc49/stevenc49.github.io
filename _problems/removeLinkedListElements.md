---
layout: page
title:  Remove Linked List Elements
last_solved: 2020-07-20
category: linkedlist
leetcode_url: https://leetcode.com/problems/remove-linked-list-elements/
status: Attempted
---

Problem
-------

```
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

```

Solution
----------

I wasn't able to solve this, despite it being easy.
There were tricks that I didn't utilized like dummy and previous pointers.
Also, my problem with linked list problems have always been edge cases.

The only way to fix this is to solve more linked list problems.

{% highlight python %}

def removeElements(self, head: ListNode, val: int) -> ListNode:
            
    dummy = ListNode(0)
    dummy.next = head
    curr, prev = head, dummy
    
    while curr:
    
        if curr.val==val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
            
    return dummy.next
    
    
{% endhighlight %}


![image1]()