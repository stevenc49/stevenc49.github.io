---
layout: page
title:  Kth Largest Element in an Array
last_solved: 
category: heap
leetcode_url: https://leetcode.com/problems/kth-largest-element-in-an-array/
status: Attempted
---

Problem
-------

```
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

```

Solution
----------

- If you're trying to find the largest kth element, use a min heap.
- As you're adding elements, evict elements if length is greater than k
- The result is the kth largest element sitting at the root

{% highlight python %}

def findKthLargest(self, nums: List[int], k: int) -> int:
    
    min_heap = []
    
    for n in nums:
        
        heapq.heappush(min_heap, n)
        
        print(min_heap) # added element n
        
        # if len>5, pop the smallest element (make room for a LARGER one)
        if len(min_heap)>k:
            heapq.heappop(min_heap)
        
        print(min_heap)
        print()
        
    return heapq.heappop(min_heap)

{% endhighlight %}

```

Your input
[3,2,1,5,6,4]
k=2

stdout
[3]
[3]

[2, 3]
[2, 3]

[1, 3, 2]
[2, 3]

[2, 3, 5]
[3, 5]

[3, 5, 6]
[5, 6]

[4, 6, 5]
[5, 6]

```

![image1]()