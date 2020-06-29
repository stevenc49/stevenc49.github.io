---
layout: page
title:  Perfect Squares
last_solved: 2020-06-28
category: dp
leetcode_url: https://leetcode.com/problems/perfect-squares/
status: Semi-Solved
---

Problem
-------

```
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

```



Solution
----------

This is suppose to be similar to the coin change problem somehow.

```

1 -> 1  (1)
2 -> 2  (1+1)
3 -> 3  (1+1+1)
4 -> 1  (4)
5 -> 2  (4+1)
6 -> 3  (4+1+1)
7 -> 4	4+1+1+1 
8 -> 2	4+4



f(1) = 1
f(2) = f(1) + f(1) = 1+1=2

f(7) = f(4) + f(3) = 1+3=4
f(8) = f(4) + f(4) = 1+1=2
f(12) = f(8) + f(4) = 2+1=3

identify subproblems?

https://leetcode.com/problems/perfect-squares/discuss/696436/Python-Simple-DP-Solution

n=7
square_sums = [0,1,4] 
dp = [0, inf, inf, inf, inf, inf, inf, inf]

      0  1  2  3  4  5  6  7
dp = [0, 1, 2, 3, 1, 2, 3, 4]

dp = [0, 1, inf, inf, 1, inf, inf, inf]

i: 1->n
iter all squares
min( dp[i], dp[i-square] )

```

{% highlight python %}

def numSquares(self, n: int) -> int:
    ## RC ##
    ## APPROACH : DP ##
    
    ## TIME COMPLEXITY : O(N^2) ##
    ## SPACE COMPLEXITY : O(N) ##

    if( n < 3) : return n
    square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
    
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for square in square_nums:
            if(i < square): break
            dp[i] = min(dp[i], dp[i-square] + 1)    # +1 is for that square we are substracting.
    return dp[-1]

{% endhighlight %}


![image1]()