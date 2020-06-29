---
layout: page
title:  Coin Change
last_solved: 
category: dp
leetcode_url: https://leetcode.com/problems/coin-change
status: Not Solved
---

```
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1

```

The solution is to build an array where the current index tells you what's the minimum # of coin for the current index(amount).
Ie: arr[2] = 1 will mean 1 coin is needed for $2.

The key formula is ```min_coins[i] = min(min_coins[i], min_coins[i - c] + 1)```


{% highlight python %}

coins = [1,2,5]
amount = 11


def coinChange(coins, amount):
        if not amount: return 0
        min_coins = [0] + [float('inf')] * amount

        for c in coins:
            for i in range(c, amount + 1):
                min_coins[i] = min(min_coins[i], min_coins[i - c] + 1)  # current val is min of current val or current val - coin + 1

        return min_coins[-1] if min_coins[-1] != float('inf') else -1




print(coinChange(coins, amount))

{% endhighlight %}


This is the printouts as you loop thru with:
```print(c, i, min_coins, min_coins[i], min_coins[i-c])```

{% highlight text %}

1 1 [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf] inf 0
1 1 [0, 1, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf] 1 0

1 2 [0, 1, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf] inf 1
1 2 [0, 1, 2, inf, inf, inf, inf, inf, inf, inf, inf, inf] 2 1

1 3 [0, 1, 2, inf, inf, inf, inf, inf, inf, inf, inf, inf] inf 2
1 3 [0, 1, 2, 3, inf, inf, inf, inf, inf, inf, inf, inf] 3 2

1 4 [0, 1, 2, 3, inf, inf, inf, inf, inf, inf, inf, inf] inf 3
1 4 [0, 1, 2, 3, 4, inf, inf, inf, inf, inf, inf, inf] 4 3

1 5 [0, 1, 2, 3, 4, inf, inf, inf, inf, inf, inf, inf] inf 4
1 5 [0, 1, 2, 3, 4, 5, inf, inf, inf, inf, inf, inf] 5 4

1 6 [0, 1, 2, 3, 4, 5, inf, inf, inf, inf, inf, inf] inf 5
1 6 [0, 1, 2, 3, 4, 5, 6, inf, inf, inf, inf, inf] 6 5

1 7 [0, 1, 2, 3, 4, 5, 6, inf, inf, inf, inf, inf] inf 6
1 7 [0, 1, 2, 3, 4, 5, 6, 7, inf, inf, inf, inf] 7 6

1 8 [0, 1, 2, 3, 4, 5, 6, 7, inf, inf, inf, inf] inf 7
1 8 [0, 1, 2, 3, 4, 5, 6, 7, 8, inf, inf, inf] 8 7

1 9 [0, 1, 2, 3, 4, 5, 6, 7, 8, inf, inf, inf] inf 8
1 9 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, inf, inf] 9 8

1 10 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, inf, inf] inf 9
1 10 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, inf] 10 9

1 11 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, inf] inf 10
1 11 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 11 10

2 2 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 2 0
2 2 [0, 1, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11] 1 0

2 3 [0, 1, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11] 3 1
2 3 [0, 1, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11] 2 1

2 4 [0, 1, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11] 4 1
2 4 [0, 1, 1, 2, 2, 5, 6, 7, 8, 9, 10, 11] 2 1

2 5 [0, 1, 1, 2, 2, 5, 6, 7, 8, 9, 10, 11] 5 2
2 5 [0, 1, 1, 2, 2, 3, 6, 7, 8, 9, 10, 11] 3 2

2 6 [0, 1, 1, 2, 2, 3, 6, 7, 8, 9, 10, 11] 6 2
2 6 [0, 1, 1, 2, 2, 3, 3, 7, 8, 9, 10, 11] 3 2

2 7 [0, 1, 1, 2, 2, 3, 3, 7, 8, 9, 10, 11] 7 3
2 7 [0, 1, 1, 2, 2, 3, 3, 4, 8, 9, 10, 11] 4 3

2 8 [0, 1, 1, 2, 2, 3, 3, 4, 8, 9, 10, 11] 8 3
2 8 [0, 1, 1, 2, 2, 3, 3, 4, 4, 9, 10, 11] 4 3

2 9 [0, 1, 1, 2, 2, 3, 3, 4, 4, 9, 10, 11] 9 4
2 9 [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 10, 11] 5 4

2 10 [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 10, 11] 10 4
2 10 [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 11] 5 4

2 11 [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 11] 11 5
2 11 [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6] 6 5

5 5 [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6] 3 0
5 5 [0, 1, 1, 2, 2, 1, 3, 4, 4, 5, 5, 6] 1 0

5 6 [0, 1, 1, 2, 2, 1, 3, 4, 4, 5, 5, 6] 3 1
5 6 [0, 1, 1, 2, 2, 1, 2, 4, 4, 5, 5, 6] 2 1

5 7 [0, 1, 1, 2, 2, 1, 2, 4, 4, 5, 5, 6] 4 1
5 7 [0, 1, 1, 2, 2, 1, 2, 2, 4, 5, 5, 6] 2 1

5 8 [0, 1, 1, 2, 2, 1, 2, 2, 4, 5, 5, 6] 4 2
5 8 [0, 1, 1, 2, 2, 1, 2, 2, 3, 5, 5, 6] 3 2

5 9 [0, 1, 1, 2, 2, 1, 2, 2, 3, 5, 5, 6] 5 2
5 9 [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 5, 6] 3 2

5 10 [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 5, 6] 5 1
5 10 [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 6] 2 1

5 11 [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 6] 6 2
5 11 [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3] 3 2

3


{% endhighlight %}

![image1]()