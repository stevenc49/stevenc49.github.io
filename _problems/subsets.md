---
layout: page
title:  Subsets
last_solved: 2020-06-22
category: recursion, backtracking
leetcode_url: https://leetcode.com/problems/subsets/
status: Solved
---

Problem
-------

```
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

```

Solution
----------

All backtracking problems have this structure, just memorize it.

{% highlight python %}

def subsets(nums):

    def backtrack(startIndex, currentSubset, allSubsets, nums):

        allSubsets.append(currentSubset)

        for i in range(startIndex, len(nums)):
            currentSubset.append(nums[i])
            backtrack( i+1, currentSubset, allSubsets, nums)
            currentSubset.remove( currentSubset[-1] )

    allSubsets = []
    backtrack( 0, [], allSubsets, nums )
    return allSubsets

{% endhighlight %}


![image1]()