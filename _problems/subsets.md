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

Still not sure why we +1 to index and why that is different from Permutation.

{% highlight python %}

def subsets3(nums):

    def backtrack(currentSubset, allSubsets, nums, index):

        allSubsets.append( currentSubset.copy() )

        for i in range(index, len(nums)):

            currentSubset.append(nums[i])
            print(currentSubset)

            backtrack( currentSubset, allSubsets, nums, i+1 )
            currentSubset.pop()
            print(currentSubset)


    ans = []
    backtrack([], ans, nums, 0)
    return ans

{% endhighlight %}


printing the currentSubset at each iteration looks like this:
```
[1]
[1, 2]
[1, 2, 3]
[1, 2]
[1]
[1, 3]
[1]
[]
[2]
[2, 3]
[2]
[]
[3]
[]
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
```

![image1]()