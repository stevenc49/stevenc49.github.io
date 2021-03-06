---
layout: page
title:  Remove Nth Node from End of List
last_solved: 2020-06-06
category: linked list
leetcode_url: https://leetcode.com/problems/remove-nth-node-from-end-of-list
status: Solved
---

Problem
-------

```
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

```

Solution
----------

{% highlight python %}

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    
    if not head: return None
    if head.next is None: return None
    
    slow = head
    fast = head
    
    # move fast up n times
    for _ in range(n):
        fast = fast.next
    
    
    # This situation would happen when we are required to del the first node (n = len(List))
    # Also, it can handle the [] case
    if not fast:
        return slow.next
    
    # move fast to the last node
    while fast.next:
        slow = slow.next
        fast = fast.next
        
    # do removal
    slow.next = slow.next.next
    
    return head

{% endhighlight %}

______________

With dummy node. Dummy node helps with edge case where you want to remove the first element.

{% highlight python %}

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

    dummy = ListNode(0)
    dummy.next = head
    
    slow, fast = dummy, dummy
    
    # advance fast pointer so gap between slow and fast are n apart
    for _ in range(n+1):
        fast = fast.next
    
    
    # advance both pointers, maintain gap
    while fast:
        slow = slow.next
        fast = fast.next
    

    # remove the nth node
    slow.next = slow.next.next
    
    return dummy.next

{% endhighlight %}

![image1]()