---
layout: page
title:  Single Number
last_solved: 2020-06-02
category: array, bit manipulation
leetcode_url: https://leetcode.com/problems/single-number/
status: Solved
---

Problem
------------

{% highlight text %}

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

{% endhighlight %}

Solution
---------

### XOR Solution


Since XOR is commutative and any number XOR'ed with itself is 0, it will cancel out all the duplicate numbers, leaving the single number by itself

{% highlight python %}

def singleNumber(self, nums: List[int]) -> int:
    
    res=0
    for n in nums:
        res = res^n
        print(res)
        
    return res

{% endhighlight %}


![image1]()