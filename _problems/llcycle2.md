---
layout: page
title:  Linked List Cycle II
last_solved: 2020-06-25
category: linked list, cycle detection
leetcode_url: https://leetcode.com/problems/linked-list-cycle-ii
status: Attempted
---

Problem
-------

```
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

```

Solution
----------

Here's the correct algorithm (similiar to [Find the Duplicate Number](/problems/findTheDuplicateNumber)). However, since we're dealing with linked lists, we have to do error checks.

{% highlight python %}

def detectCycle(self, head: ListNode) -> ListNode:
    
    slow = head
    fast = head
    
    # find intersection in cycle
    while True:
        slow = slow.next
        fast = fast.next.next
        
        if slow is fast:
            break
    
    
    # reset slow back to head and find entrance
    # the gap between the beginning and entrance == gap between fast and entrance
    # (this only applies if fast moved 2x as fast as slow)
    slow = head
    while slow!=fast:
        slow = slow.next
        fast = fast.next
    
    return slow

{% endhighlight %}

_____________________


After adding null checks and followed the tips from [Linked List Cycle I](/problems/llcycle)

{% highlight python %}

def detectCycle(self, head: ListNode) -> ListNode:
    
    if not head: return None
    
    slow = head
    fast = head
    
    # find intersection in cycle
    while True:
        
        if slow is None or fast is None or fast.next is None:
            return None
        
        slow = slow.next
        fast = fast.next.next
        
        if slow is fast:
            break
    
    
    # reset slow back to head and find entrance
    # the gap between the beginning and entrance == gap between fast and entrance
    # (this only applies if fast moved 2x as fast as slow)
    slow = head
    while slow!=fast:
        slow = slow.next
        fast = fast.next
    
    return slow

{% endhighlight %}

![image1]()