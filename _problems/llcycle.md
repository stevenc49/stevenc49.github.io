---
layout: page
title:  Linked List Cycle
---

##### hashmap solution

{% highlight python %}

    def hasCycle(self, head: ListNode) -> bool:

        if not head:
            return False
        
        seen = set()
        
        while head:
            if head in seen:
                return True
            else:
                seen.add(head)
            
            head=head.next
        
        return False

{% endhighlight %}

##### flodd - problem

Run into some infinite loops and wrong answer with input [1,2] with no cycles.
Turns outs slow and fast needs to be advanced at same time.

{% highlight python %}

def hasCycle(head):

    if not head:
        return False
    
    slow = head
    fast = head.next
    
    while fast:

        if slow is fast:
            return True

        if slow:
            slow=slow.next
            
            if fast and fast.next:
                fast=fast.next.next            
        
    return False

{% endhighlight %}

![image1]()