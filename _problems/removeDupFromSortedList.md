---
layout: page
title:  Remove Duplicate from Sorted List
last_solved: 2020-06-03
category: array, 2ptr
leetcode_url: https://leetcode.com/problems/remove-duplicates-from-sorted-array
status: Solved
---

Problem
-------

```
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

```

Solution
----------

{% highlight python %}

def removeDuplicates(self, nums: List[int]) -> int:

    if not nums: return 0
    
    # [1,1,2]
    # [0,0,1,1,1,2,2,3,3,4],
    
    slow, fast = 0, 0
    
    while fast<len(nums):
        
        # move fast until different num 
        if nums[fast]==nums[slow]:
            fast+=1
        else:
            slow+=1
            nums[slow]=nums[fast]

        #print(slow, fast, nums)
            
    return slow+1

{% endhighlight %}


![image1]()