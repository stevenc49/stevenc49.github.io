---
layout: page
title:  Move Zeros
last_solved: 2020-06-02
category: arrays
leetcode_url: https://leetcode.com/problems/move-zeroes/
status: Solved
---

Problem
-------

{% highlight text %}

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

{% endhighlight %}

Solution
----------

- Use two pointers, one to keep track of last location and another to find nonZeros
- Move nonZeros to front (oveeride)
- fill the rest of the array with zeros

{% highlight python %}

def moveZeroes(self, nums: List[int]) -> None:
    
    lastNonZero = 0
    fast = 0
    
    # move nonZeros to front (override)
    while fast<len(nums):
        
        if nums[fast]!=0:
            nums[lastNonZero] = nums[fast]
            lastNonZero+=1
        
        fast+=1
    
    # fill up the rest of array with zeros
    while lastNonZero<len(nums):
        nums[lastNonZero]=0
        lastNonZero+=1
        
    
    print(nums, lastNonZero)
    

{% endhighlight %}


![image1]()