---
layout: page
title:  Merge K Sorted Linked Lists
last_solved: 2020-08-09
category: heap
leetcode_url: https://leetcode.com/problems/merge-k-sorted-lists/
status: Solved
---

Problem
-------

```
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

```

Solution
----------


1) Push all elements into a minHeap.
2) Pop them out and create a new linked list.

time is O(n*logk) where n=total number of elements in k list
space is O(n) to hold all elements in minHeap

{% highlight python %}

def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    
            
    minHeap = []
    
    # push all elements into minHeap
    for currList in lists:
        
        head = currList
        
        while head:
            heapq.heappush(minHeap, head.val)
            head = head.next
    
    
    # pop all elements from minHeap (and craete new linked list)
    dummy = ListNode(0)
    head = dummy
    
    while minHeap:
        head.next = ListNode( heapq.heappop(minHeap) )
        head = head.next
        
    return dummy.next


{% endhighlight %}


![image1]()