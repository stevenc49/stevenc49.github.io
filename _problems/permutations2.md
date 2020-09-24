---
layout: page
title:  Permutations II
last_solved: 2020-09-24
category: recursion, backtracking
leetcode_url: https://leetcode.com/problems/permutations-ii
status: Solved
---

Problem
-------

```
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

```

Solution
----------

This solution works for small cases but TLE on larger cases

{% highlight python %}

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        
        output = []
        
        def backtrack(currentList):
            
            if len(currentList)==len(nums):
                
                if sorted(currentList)==sorted(nums) and currentList not in output:
                    output.append(currentList.copy())

                return
            
            
            for i in range(0, len(nums)):
                
                currentList.append(nums[i])
                backtrack(currentList)
                currentList.pop()
        
        backtrack([])
        return output
    

{% endhighlight %}

![image1](https://i.ibb.co/S7488mz/16009729542977295723811940825272.jpg)