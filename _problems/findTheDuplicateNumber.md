---
layout: page
title:  Find the Duplicate Number
last_solved: 2020-06-25
category: cycle detection
leetcode_url: https://leetcode.com/problems/find-the-duplicate-number
status: Attempted
---

Problem
-------

```
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

```

Solution
----------

{% highlight python %}

def findDuplicate(self, nums: List[int]) -> int:
    
    slow = nums[0]
    fast = nums[0]
    
    # find intersection point of 2 ptrs in cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
    
        if slow==fast:
            break
            
    # key point: after they meet in cycle, the gap between beginning to entrance and where fast pointer resides to entrace are equal
    
    # find the entrace
    slow = nums[0]  # reset slow back to beginning
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return fast

{% endhighlight %}


![image1]()