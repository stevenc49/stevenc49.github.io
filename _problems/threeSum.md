---
layout: page
title:  Three Sum
last_solved: 2020-07-08
category: array
leetcode_url: https://leetcode.com/problems/3sum
status: Not Attempted
---

Problem
-------

```
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

```

Solution
----------

__________

This triple loop solution will cause duplicates sets.

{% highlight python %}

ans = []
for i in range(len(nums)):
    for j in range(i, len(nums)):
        for k in range(j, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                ans.append([nums[i], nums[j], nums[k]])

{% endhighlight %}

__________


Check out [dicussion](https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)) and [timonthy's video](https://www.youtube.com/watch?v=LBOAVbEqOTQ)

When I tried to mimic that solution on my own:


{% highlight python %}

def threeSum(nums):

    nums.sort()
    output = []

    print(nums)

    index = 0
    while index<len(nums):

        fixed = nums[index]     # -1
        target = fixed*-1       # want to find 1 in rest of array

        l,r = index+1, len(nums)-1

        while l<r:

            if nums[index] + nums[l] + nums[r] == 0:
                output.append( [nums[index], nums[l], nums[r]] )
            
            l+=1
            r-=1
        

        index+=1
    
    return output

{% endhighlight %}

It will pass the first case:
[-4, -1, -1, 0, 1, 2]
[[-1, -1, 2], [-1, 0, 1]]

But will create a duplicate set on:
[0, 0, 0, 0]
[[0, 0, 0], [0, 0, 0]]

__________


![image1]()