---
layout: page
title:  Permutations
last_solved: 2020-06-22
category: recursion, backtracking
leetcode_url: https://leetcode.com/problems/permutations
status: Attempted
---

Problem
-------

```
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

```

Solution
----------

A generic backtracking skeleton is [here](https://leetcode.com/problems/permutations/discuss/18239/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partioning))

```
    """
    Level0: []
    level1: [1]                  [2]              [3]
    level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
    level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]          
    
    """
```    

{% highlight python %}

nums = [1,2,3]

def backtracking(res,visited,subset,nums):
    if len(subset) == len(nums):
        res.append(subset)
    for i in range(len(nums)):
        if i not in visited:
            visited.add(i)
            backtracking(res,visited,subset+[nums[i]],nums)
            visited.remove(i)

def permute(nums):
    visited = set()
    res = []
    backtracking(res,visited,[],nums)
    return res

print(permute(nums))

{% endhighlight %}


![image1]()