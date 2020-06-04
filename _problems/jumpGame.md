---
layout: page
title:  Jump Game
last_solved: 2020-06-04
category: greedy, dp, backtracking
leetcode_url: https://leetcode.com/problems/jump-game
status: Semi-Solved, Multiple solutions
---

Problem
-------

```
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

```

Solution
----------

There are 4 solutions to this:
- backtracking
- dp - top down
- dp - bottom up
- greedy


The solutions article in leetcode is actually really good for this question. [here](https://leetcode.com/problems/jump-game/solution/)

#### Greedy Approach

Go backwards from the last position. If you can reach the first element from the last element, then you are good.

This is a O(n) time and O(1) space solution.

{% highlight python %}

def canJump(self, nums: List[int]) -> bool:
    
    lastPos = len(nums) - 1
    for i in reversed(range(len(nums))):
        
        if i + nums[i] >= lastPos:
            lastPos = i
    
    return lastPos == 0

{% endhighlight %}


![image1]()