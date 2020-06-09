---
layout: page
title:  Search in Rotated Sorted Array
last_solved: 2020-06-07
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

Check Nick White's video on this question. it's also 2-pass binary search

{% highlight python %}

def search(self, nums, target):
    if not nums:
        return -1
    l,r=0,len(nums)-1
    while l<=r:
        m=(l+r)/2
        if nums[m]<nums[0]:
            r=m-1
        else:
            l=m+1

    if nums[0]>target:
        r=len(nums)-1
    else:
        l=0
    
    while l<=r:
        m=(l+r)/2
        if nums[m]==target:
            return m
        if nums[m]<target:
            l=m+1
        else:
            r=m-1
    return -1

{% endhighlight %}


![image1]()