---
layout: page
title:  Combination Sum
last_solved: 2020-06-27
category: permutations
leetcode_url: https://leetcode.com/problems/combination-sum/
status: Attempted
---

Problem
-------

```
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

```

Solution
----------

{% highlight python %}

candidates = [2,3,6,7]
target = 7

def combinationSum(candidates, target):
    
    def backtrack(currentList, nums, start):
        
        if sum(currentList)==target:
            allValidCombos.append( currentList.copy() )
            return 
        if sum(currentList) > target: # optimization
            return
        for i in range(start, len(nums)):
            backtrack(currentList + [nums[i]], nums, i)
            # currentList.append( nums[i] )
            # backtrack( currentList, nums, start)
    
    allValidCombos = []
    backtrack([], candidates, 0 )
    return allValidCombos

print( combinationSum(candidates, target) )

{% endhighlight %}


![image1]()