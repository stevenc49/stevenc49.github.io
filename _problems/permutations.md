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

```
[10]
[10, 10]
[10, 10, 10]
[10, 10]
[10, 10, 20]
[10, 10]
[10, 10, 30]
[10, 10]
[10]
[10, 20]
[10, 20, 10]
[10, 20]
[10, 20, 20]
[10, 20]
[10, 20, 30]
[10, 20]
[10]
[10, 30]
[10, 30, 10]
[10, 30]
[10, 30, 20]
[10, 30]
[10, 30, 30]
[10, 30]
[10]
[]
[20]
[20, 10]
[20, 10, 10]
[20, 10]
[20, 10, 20]
[20, 10]
[20, 10, 30]
[20, 10]
[20]
[20, 20]
[20, 20, 10]
[20, 20]
[20, 20, 20]
[20, 20]
[20, 20, 30]
[20, 20]
[20]
[20, 30]
[20, 30, 10]
[20, 30]
[20, 30, 20]
[20, 30]
[20, 30, 30]
[20, 30]
[20]
[]
[30]
[30, 10]
[30, 10, 10]
[30, 10]
[30, 10, 20]
[30, 10]
[30, 10, 30]
[30, 10]
[30]
[30, 20]
[30, 20, 10]
[30, 20]
[30, 20, 20]
[30, 20]
[30, 20, 30]
[30, 20]
[30]
[30, 30]
[30, 30, 10]
[30, 30]
[30, 30, 20]
[30, 30]
[30, 30, 30]
[30, 30]
[30]
[]
```

________________________


Following the generic backtracking structure:

{% highlight python %}

def permute(nums):

    def backtrack(currentList, allPermutations, nums):

        if len(currentList)==len(nums):
            allPermutations.append(currentList[:])  # or currentList.copy() because Python passes by reference
        else:
            for i in range(0, len(nums)):
                if nums[i] in currentList:
                    continue
                currentList.append(nums[i])
                backtrack( currentList, allPermutations, nums )
                currentList.remove(currentList[-1])     # currentList.pop() also does the same thing

    allPermutations = []
    backtrack([], allPermutations, nums)
    return allPermutations

{% endhighlight %}

_________


{% highlight python %}

def permute(self, nums: List[int]) -> List[List[int]]:
    
    def backtrack(index, currentList, nums, output):
        
        # base case
        if len(currentList)==len(nums):
            output.append( currentList.copy() )
        else:
            
            for i in range(len(nums)):
                
                if nums[i] not in currentList:
                    currentList.append( nums[i] )
                    backtrack( index+1, currentList, nums, output )
                    currentList.pop()
    
    output = []
    backtrack(0, [], nums, output)
    return output

{% endhighlight %}

![image1]()