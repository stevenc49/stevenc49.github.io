---
layout: page
title:   Increasing Triplet Subsequence
last_solved: 2020-07-05
category: dp
leetcode_url: https://leetcode.com/problems/increasing-triplet-subsequence
status: Attempted
---

Problem
-------

```
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false

```

Solution
----------

Initially tried this, but it would fail for ```[2,5,3,4,5]```

{% highlight python %}

    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if not nums: return false
        
        first = nums[0]
        second = None
        third = None
        
        for i in range(1, len(nums)):
            
            if first and not second and not third and nums[i]>first:
                second = nums[i]
            elif first and second and not third and nums[i]>second:
                third = nums[i]
        
        
        print(first, second, third)
        return True if third else False
        

{% endhighlight %}

Looks like the way to approach this is similiar to the LIS (Longest increasing subsequence) problem.

[A simpler solution involving thresholds](https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78995/Python-Easy-O(n)-Solution/373508)

![image1]()