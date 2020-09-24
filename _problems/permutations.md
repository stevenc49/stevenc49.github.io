---
layout: page
title:  Permutations
last_solved: 2020-06-22
category: recursion, backtracking
leetcode_url: https://leetcode.com/problems/permutations
status: Solved
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


[medium article on permutation/subsets](https://medium.com/algorithms-and-leetcode/backtracking-e001561b9f28)


```
    """
    Level0: []
    level1: [1]                  [2]              [3]
    level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
    level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]          
    
    """
```    

The vanilla backtracking template would do this to `currList`.
So that's why you need to check to that nums[i] is not in `currList`


________________________


Following the generic backtracking structure:

_________


{% highlight python %}

def permute(nums):

    output = []

    def backtrack(currentList):

        print(currentList)

        # base case
        if len(currentList)==len(nums):
            output.append(currentList.copy())
        
        # imagine you're at [1] (your currentList) and you want to append 1,2,3 to your child branches
        # so they become 11, 12, 13
        for i in range(0, len(nums)):

            if nums[i] in currentList:
                continue

            currentList.append(nums[i])
            backtrack(currentList)
            currentList.pop()
    
    backtrack([])
    return output

{% endhighlight %}

![image1](https://i.ibb.co/S7488mz/16009729542977295723811940825272.jpg)