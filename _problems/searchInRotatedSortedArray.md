---
layout: page
title:  Search in Rotated Sorted Array
last_solved: 
category: binary search
leetcode_url: https://leetcode.com/problems/search-in-rotated-sorted-array
status: Attempted
---

Problem
-------

```
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

```

Solution
----------

Do it in two parts:
- first find pivot (similar to find min in rotated sorted array)
- then reset boundaries to do a regular binary search

{% highlight python %}

def search(self, nums: List[int], target: int) -> int:
    
    if not nums: return -1
    
    left, right = 0, len(nums)-1

    # get left to the pivot
    while left<right:

        mid = (left+right)//2

        if nums[mid]<nums[right]:   # this is the condition that we want to satisfy w.r.t. mid

            right = mid

        else:

            left = mid+1

    # left is pivot
    start = left
    left = 0
    right = len(nums)-1
    
    # target is on right side
    if target>=nums[start] and target<=nums[right]:
        left = start
    else:   # target is on left side
        right = start
    
    
    # do binary search
    while left<=right:
        
        mid = (left+right)//2
        
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left = mid+1
        else:
            right = mid-1
    
    return -1
    

{% endhighlight %}


![image1]()