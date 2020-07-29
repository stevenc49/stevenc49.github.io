---
layout: page
title:  Find First and Last Position of Element in Sorted Array
last_solved: 
category: binary search
leetcode_url: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
status: Attempted
---

Problem
-------

```
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

```

Solution
----------

[nick white](https://www.youtube.com/watch?v=bU-q1OJ0KWw)

Run binary search twice:
- find the starting position
- find the ending position

Take note of boundary conditions and termination conditions when implementing binary search.

{% highlight python %}

def searchRange(self, nums: List[int], target: int) -> List[int]:

    def findStartIndex(nums, target):
        
        index = -1
        
        left, right = 0, len(nums)-1

        while left<=right:

            mid = left + (right-left) // 2
            if nums[mid]>=target:   # >= becuz we want to find teh first occurance of the duplicates
                right = mid-1
            else:
                left = mid+1

            if nums[mid]==target:
                index = mid
        
        return index
    
    
    
    def findEndIndex(nums, target):
        
        index = -1
        
        left, right = 0, len(nums)-1

        while left<=right:

            mid = left + (right-left) // 2
            if nums[mid]<=target:
                left = mid+1
            else:
                right = mid-1

            if nums[mid]==target:
                index = mid
        
        return index
        
    start = findStartIndex(nums, target)
    end = findEndIndex(nums, target)
    
    return [start,end]

{% endhighlight %}


![image1]()