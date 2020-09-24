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


________________


To combat TLE, I added a visited set to prune the recursion tree.

{% highlight python %}

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        output = []        
        visited = set()
        
        def backtrack(currentList):
            
            # this caches visited nodes so we don't go down duplicated recursion trees
            if tuple(currentList) in visited:
                return
            else:
                visited.add(tuple(currentList))
            
            
            # base case
            if len(currentList)==len(nums):

                # when these conditions are met, add it to output
                if sorted(currentList)==sorted(nums) and currentList not in output:
                    output.append(currentList.copy())

                return

            #  going down the recursion tree (similar to permutation 1 but without duplicate check)
            for i in range(0, len(nums)):

                currentList.append(nums[i])
                backtrack(currentList)
                currentList.pop()
        
        backtrack([])
        return output

{% endhighlight %}

![image1](https://i.ibb.co/8XfLcRH/16009806513183664237674845577197.jpg)