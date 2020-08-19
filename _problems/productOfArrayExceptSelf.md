---
layout: page
title:  Product of Array Except Self
last_solved: 
category: 
leetcode_url: https://leetcode.com/problems/product-of-array-except-self
status: Attempted
---

Problem
-------

```
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

```

Solution
----------

Make Left and Right Array, then multiply together.

= Left Array consist of product of all elements to the left of i
- Right Array consist of product of all elements to the right of i

{% highlight python %}

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        
        L, R, ans = [0]*length, [0]*length, [0]*length
        
        L[0]=1
        for i in range(1, length):
            L[i] = nums[i-1]*L[i-1]
        
        R[length-1]=1
        for i in range(length-2, -1, -1):
        # for i in reversed(range(length-1)):
            R[i] = nums[i+1] * R[i+1]
        
        
        for i in range(length):
            ans[i] = L[i]*R[i]
        
        return ans

{% endhighlight %}


![image1]()