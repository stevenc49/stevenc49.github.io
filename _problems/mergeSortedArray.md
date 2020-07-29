---
layout: page
title:  Merge Sorted Array
last_solved: 
category: 
leetcode_url: https://leetcode.com/problems/merge-sorted-array/
status: Attempted
---

Problem
-------

```
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

```

Solution
----------

{% highlight python %}

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    
    # nums1 = [1,2,3,0,0,0], m = 3
    # nums2 = [2,5,6],       n = 3
    
    # start from the back (avoid overwriting)
    i = m-1
    j = n-1
    
    end = len(nums1)-1
    
    while i>=0 and j>=0:
        
        if nums2[j]>=nums1[i]:
            nums1[end] = nums2[j]
            j-=1
        else:
            nums1[end] = nums1[i]
            i-=1
        
        end-=1

    # this part need to take care of edge case with nums1=[0] and nums2=[1]
    if i==-1:
        nums1[:j+1] = nums2[:j+1]

{% endhighlight %}


![image1]()