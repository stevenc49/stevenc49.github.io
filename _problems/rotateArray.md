---
layout: page
title:  Rotate Array
last_solved: 2020-06-04
category: array
leetcode_url: https://leetcode.com/problems/rotate-array/
status: Semi-Solved, Multiple solutions
---

Problem
-------

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

```

Solution
----------

There are at least 4 solutions:
- brute force
- use extra space
- using cyclic replacement?
- 2 pass reversal


#### 2 pass reversal approach

{% highlight python %}

def rotate(self, nums: List[int], k: int) -> None:
    
    if not nums: return
    if len(nums)==1: return
    
    # in case k>len(nums)
    if k>len(nums):
        k = k%len(nums)
    
    def reverse(nums, start, end):
        
        while start<end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
        
            start+=1
            end-=1

    
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)
    

{% endhighlight %}


![image1]()