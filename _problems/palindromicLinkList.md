---
layout: page
title:  Palindrome Linked List
last_solved: 2020-07-22
category: linked lists, palindrome
leetcode_url: https://leetcode.com/problems/palindrome-linked-list/
status: Attempted
---

Problem
-------

```
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

```

Solution
----------

- Have a slow and fast poiner, and find middle.
- Once at middle, reverse the second half of the list
- Then Iterate both first half and second half to ensure they are the same

Note:
- Whichever pointer gets to the end of the list first, make that your break condition (in while loop)

{% highlight python %}

def isPalindrome(self, head: ListNode) -> bool:
    
    
    def reversed(head):
        
        prev = None
        curr = head
        next = None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
    
    # find mid
    slow = head
    fast = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    # reverse second half of list
    slow = reversed(slow)
    fast = head
    
    # iterate both slow and fast and make sure they're the same
    while slow:
        
        if slow.val!=fast.val:
            return False
        slow = slow.next
        fast = fast.next
    
    return True
    


{% endhighlight %}


![image1]()