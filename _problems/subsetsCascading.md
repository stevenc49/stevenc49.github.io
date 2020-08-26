---
layout: page
title:  Subsets (Cascading)
last_solved: 2020-06-22
category: cascading
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



Another way is the BFS approach from [educative](https://www.educative.io/courses/grokking-the-coding-interview/gx2OqlvEnWG)




```

Given set: [1, 5, 3]

Start with an empty set: [[]]
Add the first number (1) to all the existing subsets to create new subsets: [[], [1]];
Add the second number (5) to all the existing subsets: [[], [1], [5], [1,5]];
Add the third number (3) to all the existing subsets: [[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3]].

```


{% highlight python %}

def find_subsets(nums):
  subsets = []
  # start by adding the empty subset
  subsets.append([])
  for currentNumber in nums:
    # we will take all existing subsets and insert the current number in them to create new subsets
    n = len(subsets)
    for i in range(n):
      # create a new subset from the existing subset and insert the current element to it
      set = list(subsets[i])
      set.append(currentNumber)
      subsets.append(set)

  return subsets

{% endhighlight %}


Time and space complexity is O(2^n) because we will have 2^n items



________________


{% highlight python %}

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
#         start with empty set
#         []
        
#         make a copy of all existing subsets and add 1 to them
#         [] [1]
        
#         make a copy of all existing subsets and add 2 to them
#         [] [1] [2,][1,2]
        
#         make a copy of all existing subsets and add 3 to them
#         [] [1] [2][1,2] [3] [1,3] [2,3][1,2,3]
        
    
        subsets = [[]]
        
        for n in nums:
            
            # make a copy of all existing subsets
            size = len(subsets)
            
            existingSubsets = []
            for i in range(size):
                existingSubsets.append( subsets[i].copy() )
                
            # add n to all existing subsets
            for existSubset in existingSubsets:
                existSubset.append(n)
                
            # add existing subset list into master subset list
            subsets.extend( existingSubsets )
        
        return subsets

{% endhighlight %}