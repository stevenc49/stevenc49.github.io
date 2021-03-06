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

______________

{% highlight python %}

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        
        def backtrack(currentList, start):
            
            if sum(currentList)==target:
                output.append(currentList.copy())
                return
            
            if sum(currentList) > target: # optimization
                return
            
            for i in range(start, len(candidates)):
                backtrack(currentList + [candidates[i]], i)
            
        
        backtrack([], 0)
        return output

{% endhighlight %}


____________


- [watch this explaination](https://www.youtube.com/watch?v=irFtGMLbf-s)
- [watch this too](https://www.youtube.com/watch?v=MTI2wc8s0BY)

{% highlight python %}

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        
        def backtrack(currentList, remaining, start):
        
            if remaining<0:
                return
            elif remaining==0:
                output.append(currentList.copy())
            else:
            
                for i in range(start, len(candidates)):
                    currentList.append(candidates[i])
                    backtrack(currentList, remaining-candidates[i], i)
                    currentList.pop()

        backtrack([], target, 0)
        return output

{% endhighlight %}

![image1]()