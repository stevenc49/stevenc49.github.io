---
layout: page
title:  Unique BST
last_solved: 2020-06-24
category: dp
leetcode_url: https://leetcode.com/problems/unique-binary-search-trees/
status: Attempted
---

Problem
-------

```
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

```

Solution
----------

```
For n=1: you just have 1 pattern.
For n=2, you have 2 possible patterns
For n=3,
- if you put 1 at the root, you have 2 patterns for the remaining (calculated above)
- if you put 2 at the root, you just have 1 possible pattern
- if you put 3 at the root, you have 2 patterns avaiable for the remaining numbers

f(3) = g(2) + g(1) + g(2) = 2 + 1 + 2 = 5

For n=4:

1,2,3,4
- if 1 is at root, the remaining has g(3) combinations
- if 2 is at root, [1] will have 1 combination and [3,4] will have 2 combination, you need to multiply them
- if 3 is at root, [1,2] will have g(2) combo and [4] will have 1 combo, mulitply them
- if 4 is at root, [1,2,3] has 5 combo

f(4) = g(3) + (1*g(2)) + (g(2)* 1) + g(3)
     = 5 + (1*2) + (1*2) + 5
     = 14
```


{% highlight python %}

class Solution:
    def numTrees(self, n: int) -> int:
        
        @lru_cache(None)
        def helper(left, right):
            
            # base case, g(1)
            if left>=right:
                return 1
            
            count = 0
            for i in range(left, right+1):
                l_tree = helper(left, i-1)
                r_tree = helper(i+1, right)
                count += l_tree * r_tree
            
            return count
    
        return helper(1, n)

{% endhighlight %}


![image1]()