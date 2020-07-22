---
layout: page
title:  Odd Even Linked List
last_solved: 2020-07-21
category: linked list
leetcode_url: https://leetcode.com/problems/odd-even-linked-list
status: Attempted
---

Problem
-------

```
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

```

Solution
----------

Initially tried this but it's in an endless loop

{% highlight python %}

def oddEvenList(self, head: ListNode) -> ListNode:
    
    odd = head
    even = head.next
    tmp = None
    
    while odd and odd.next:
        
        print(odd.val)
        
        tmp = odd
        
        odd.next = odd.next.next
        odd = tmp.next.next
        
        
    if odd:
        odd.next = even
    else:
        tmp.next = even
        
    while even and even.next:
        
        even.next = even.next.next
        even = even.next.next

{% endhighlight %}


![image1]()