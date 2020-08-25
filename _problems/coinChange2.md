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

[This](https://www.youtube.com/watch?v=DJ4a7cmjZY0) video from backtobackswe explains why you subtract the coin.

```
        0	1	2	3	4	5
[1]     1	1	1	1	^1^	1
[1,2]	1	1	`2`	2	*3*	3
[1,2,5]	1	1	2	2	3	4
```

```*3* = ^1^ + `2` ```

Think of "ways to make $4 with [1,2]" is equal to:

It's equal to (ways to make $4 with [1] coin) + (ways to make $2 with [1,2] coins)

```	(1+1+1+1)         +      ( [1,1] + [2] ) "+2 if we use the $2 coin"         ```

The reason it's "ways to make $2 with [1,2] coins" is because if **we USE THE 2 coin, then it's $4-$2 coin, and we solve subproblem of ways to make $2 with [1,2] coins**

{% highlight python %}

    def change(self, amount: int, coins: List[int]) -> int:

        dp = [ [1]+[0]*amount for _ in range(len(coins)+1)]
        
        for c in range(1, len(coins)+1):
            for a in range(1, amount+1):
                if coins[c-1] <= a:
                    dp[c][a] = dp[c-1][a] + dp[c][a-coins[c-1]]
                else:
                    dp[c][a] = dp[c-1][a]
        
        print(dp)
        return dp[len(coins)][amount]  # or dp[-1][-1]

{% endhighlight %}

______

This code is simplier, try to analyze this one instead

{% highlight python %}

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)             # DP Array of size (Amount +1) initialized to 0
        dp[0] = 1

        for currCoin in coins:
            for currAmount in range(currCoin, amount + 1):
                dp[currAmount] += dp[currAmount - currCoin]

        return dp[-1]

{% endhighlight %}


![image1]()