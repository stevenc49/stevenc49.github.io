---
layout: page
title:  Permutations (Cascading)
last_solved: 2020-06-22
category: cascading
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

```

Let’s take [1,3,5] as an example. Following a BFS approach, we will consider one number at a time:

If the given set is empty then we have only an empty permutation set: []
Let’s add the first element (1), the permutations will be: [1]
Let’s add the second element (3), the permutations will be: [3,1], [1,3]
Let’s add the third element (5), the permutations will be: [5,3,1], [3,5,1], [3,1,5], [5,1,3], [1,5,3], [1,3,5]
Let’s analyze the permutations in the 3rd and 4th step. How can we generate permutations in the 4th step from the permutations of the 3rd step?

If we look closely, we will realize that when we add a new number (5), we take each permutation of the previous step and insert the new number in every position to generate the new permutations. For example, inserting ‘5’ in different positions of [3,1] will give us the following permutations:

Inserting ‘5’ before ‘3’: [5,3,1]
Inserting ‘5’ between ‘3’ and ‘1’: [3,5,1]
Inserting ‘5’ after ‘1’: [3,1,5]

```


{% highlight python %}

def permute(self, nums):

    result = []
    
    permutations = []
    permutations.append([])
    
    for currNum in nums:
        
        # we will take all existing permutations and add currNum to create new permutations
        n = len(permutations)
        
        for _ in range(n):
            
            oldPermutation = permutations.pop(0)
            
            # create new permutation by adding the currNum at every position
            for j in range( len(oldPermutation)+1 ):
                
                newPermutation = list(oldPermutation)
                newPermutation.insert(j, currNum)
                
                if len(newPermutation)==len(nums):
                    result.append(newPermutation)
                else:
                    permutations.append(newPermutation)
        
    return result

{% endhighlight %}