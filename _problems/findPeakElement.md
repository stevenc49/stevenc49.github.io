---
layout: page
title:  Find Peak Element
last_solved: 
category: binary search
leetcode_url: https://leetcode.com/problems/find-peak-element/
status: Attempted
---

Problem
-------

```
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.

```

Solution
----------

Warning:
- if you have `<=` in `while left<=right` but left and right assignments do not converge to mid, then you will have infinite loop

{% highlight python %}

def findPeakElement(self, nums: List[int]) -> int:
    
    left, right = 0, len(nums)-1
    
    while left<right:  
        
        mid = left + (right-left) // 2
        
        if nums[mid] < nums[mid+1]:     # mid is sloping up
            left = mid+1                # peak can't be on left side
        else:
            right = mid               # peak can't be on right side
        
    return left

{% endhighlight %}


![image1]()