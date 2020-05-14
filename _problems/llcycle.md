---
layout: page
title:  Linked List Cycle
---

##### Hashmap solution

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

#### Flodd - buggy

Ran into some infinite loops and wrong answer with input [1,2] with no cycles.
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


#### Flodd - working

Just keep it clean and clear and keep all 1) termination checks and 2) pointer advancements together.

Some tips (to reduce chances of bugs):
- add null checks for everything that could be null (ie: slow, fast and fast.next)
- keep slow and fast pointer advancements in one if block (had bug when one was advanced but not the other)
- use While True (instead of while fast) and have return True and return False cases
- initialize slow and fast to be different, the check "if slow is fast" could get triggered too early



{% highlight python %}

def hasCycle(head):

    if not head:
        return False
    
    slow = head
    fast = head.next
    
    while True:

        # if either pointer is null, reached end of list and return False
        if slow is None or fast is None or fast.next is None:
            return False

        # cycle detected, exit and return True
        if slow is fast:
            return True 

        # advance pointers
        slow=slow.next
        fast=fast.next.next

{% endhighlight %}

![image1]()