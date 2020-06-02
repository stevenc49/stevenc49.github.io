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


### Add to List and Remove if duplicated

{% highlight python %}

def singleNumber(self, nums: List[int]) -> int:
    
    dupList = []
    
    for n in nums:
        if n in dupList:
            dupList.remove(n)
        else:
            dupList.append(n)
    
    return dupList[0]

{% endhighlight %}

- Time: O(n^2) because O(n) to look thru list once, and since search is in loop, it's another O(n)
- Space: O(n)


### Hashtable

Add to hash table with count and return count=1.

- O(n) time and space

### XOR Solution (Best Solution)


Since XOR is commutative and any number XOR'ed with itself is 0, it will cancel out all the duplicate numbers, leaving the single number by itself

- O(n) time
- O(1) space

{% highlight python %}

def singleNumber(self, nums: List[int]) -> int:
    
    res=0
    for n in nums:
        res = res^n
        print(res)
        
    return res

{% endhighlight python %}


![image1]()