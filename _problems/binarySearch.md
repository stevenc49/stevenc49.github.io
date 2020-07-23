---
layout: page
title:  Binary Search
last_solved: 2020-07-23
category: binary search
leetcode_url: https://leetcode.com/tag/binary-search/
status: Attempted
---

Problem
-------

```
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

```

Solution
----------

{% highlight python %}

def search(self, nums: List[int], target: int) -> int:
    
    def binSearch(low, high, target, nums):
        
        print(low, high, nums, target)
        
        while low<=high:
        
            mid = (low+high)//2

            if nums[mid]==target:
                return mid
            elif target>nums[mid]:  # if target is greater, ignore left half
                low = mid+1
            else:                   # if target is smaller, ignore right half
                high = mid-1
        
        return -1
    
    return binSearch(0, len(nums)-1, target, nums)

{% endhighlight %}


![image1]()