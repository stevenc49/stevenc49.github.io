---
layout: page
title:  Unique Paths
last_solved: 2020-06-29
category: dp
leetcode_url: https://leetcode.com/problems/unique-paths/submissions/
status: Solved
---

Problem
-------

```
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

 

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

```

Solution
----------

{% highlight python %}

def uniquePaths(self, m: int, n: int) -> int:
    
    dp = [[1]*(n) for x in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    print(dp)
    return dp[-1][-1]

{% endhighlight %}


![image1]()