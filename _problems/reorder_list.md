---
layout: page
title:  Reorder List
last_solved: 
category: linked list
leetcode_url: https://leetcode.com/problems/reorder-list/
status: Attempted
---

Problem
-------

```
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
```

Solution
----------

With Stack:

- make a queue(), push all nodes to it
- pop off left and right side of q, alternating each time
- as you pop off, rebuild linked list (make sure to set node.next to None)


{% highlight python %}

    def reorderList(self, head: ListNode) -> None:

        # push all into list
        q = deque()
        while head:
            q.append(head)
            head = head.next
        
        
        dummy = ListNode(0)
        cur = dummy
        even = False
        
        while q:
            
            node = q.pop() if even else q.popleft()
            node.next = None
            
            cur.next = node
            cur = cur.next
            
            even ^= True
        
        return dummy.next


{% endhighlight %}

____________

Without Stack

- split list in half
- reverse second half
- merge lists

{% highlight python %}

    def reorderList(self, head: ListNode) -> None:

        if not head: return None
        
        # 1 2 3 4
        # 8 7 6 5

        
        # 1) split list in half
        prev, slow, fast = None, head, head
        
        
        
        while fast and fast.next:
            
            prev = slow     # prev is "tail" of slow
            slow = slow.next
            fast = fast.next.next
        
        # print(prev.val, slow.val, fast)
        
        # current state
        # 1 2 3 4
        #   p s   f
        
        
        prev.next = None
        
        l1 = head
        
        # 1 2
        # l p
        #
        # 3 4
        # s f
        
        # 2) reverse second list
        def reverse(head):
            
            prev, curr, next = None, head, None
            
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            return prev
        
        
        l1 = head
        l2 = reverse(slow)
        print(l1.val, l2.val)
        
        # 1 2
        # 4 3
        
        # 3) time to merge
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            
            if l1:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            if l2:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
        
        if l1:
            curr.next = l1
        
        if l2:
            curr.next = l2
        
        return dummy.next
        


{% endhighlight %}

![image1]()