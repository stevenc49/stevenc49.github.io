---
layout: page
title:  Coin Change 2
last_solved: 2020-06-07
category: dp
leetcode_url: https://leetcode.com/problems/coin-change-2
status: Not Solved
---

Problem
-------

```
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1

```

Solution
----------

[This](https://leetcode.com/problems/coin-change-2/discuss/675096/Python-O(amount-*-N)-simple-dp-explained-(updated)) discussion explains it, but I'm still not getting how the dp table derives its values.

```
                0	1	2	3	4	5
coin #0 (1)	1	1	1	1	1	1
coin #1 (2)	1	1	2	2	3	3
coin #2 (5)	1	1	2	2	3	4
```

{% highlight python %}

def change(self, amount, coins):
    N = len(coins)
    if N == 0: return int(N == amount)
    
    dp_sum = [[0] * N for _ in range(amount + 1)]
    for i in range(N): dp_sum[0][i] = 1
    
    for i,j in product(range(amount), range(N)):
        dp_sum[i+1][j] = dp_sum[i+1][j-1]
        if i+1 - coins[j] >= 0:
            dp_sum[i+1][j] += dp_sum[i+1-coins[j]][j]           
                
    return dp_sum[-1][-1]

{% endhighlight %}


![image1]()