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


![image1]()