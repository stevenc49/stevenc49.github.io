---
layout: page
title:  Kth Largest Element in a Stream
last_solved: 
category: heap
leetcode_url: https://leetcode.com/problems/kth-largest-element-in-a-stream
status: Attempted
---

Problem
-------

```
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

```

Solution
----------

{% highlight python %}

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        
        self.nums.append(val)
        
        # we don't need to use heap, a simple sort is good enough
#         self.nums = [-abs(x) for x in self.nums]      
#         heapq.heapify(self.nums)
        
        self.nums = sorted(self.nums, reverse=True)
        
        return self.nums[self.k-1]

{% endhighlight %}


__________-


{% highlight python %}

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        # self.nums = nums
        self.nums = heapq.nlargest(self.k, nums)[::-1]
        

    def add(self, val: int) -> int:
        
        # push new element onto heap
        heapq.heappush(self.nums, val)
    
        # print(self.nums)
        
        # if length exceeds k, pop off the smallest (make room for a larger one)
        if len(self.nums)>self.k:
            heapq.heappop(self.nums)
               

        # print(self.nums)
        # print()
                
        return self.nums[0]     # kth largest element is sitting at root (min of non evicted elements)


{% endhighlight %}

![image1]()