---
layout: page
title:  Combination Sum II
last_solved: 
category: backtrack
leetcode_url: https://leetcode.com/problems/combination-sum-ii
status: Attempted
---

Problem
-------

```
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

Solution
----------



{% highlight python %}

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        candidates = sorted(candidates)
        
        def backtrack(currentList, remaining, start):
        
            if remaining<0:
                return
            elif remaining==0:
                output.append(currentList.copy())
            else:
            
                for i in range(start, len(candidates)):
                    
                    if i==start or candidates[i]!=candidates[i-1]:
                    
                        currentList.append(candidates[i])
                        backtrack(currentList, remaining-candidates[i], i+1)
                        currentList.pop()

        backtrack([], target, 0)
        return output
    

{% endhighlight %}

______________



{% highlight python %}


{% endhighlight %}

![image1]()