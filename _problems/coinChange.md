---
layout: page
title:  Coin Change
last_solved: 2020-07-17, 2020-08-25
category: dp [bottom up]
leetcode_url: https://leetcode.com/problems/coin-change
status: Solved
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



[This video](https://www.youtube.com/watch?v=jgiZlGzXMBw) actually does the best job at explaining the bottom up approach.

{% highlight python %}

    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [0] + [float('inf')] * amount
        
        for a in range(1, amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a] = min( dp[a], dp[a-c]+1 )
        
        print(dp)
        
        return dp[-1] if dp[-1]!=float('inf') else -1

{% endhighlight %}


![image1](https://5wig4g.dm.files.1drv.com/y4mboD94pR7HKG8_TUT5aIpOrHQ-N26HFp9PZXq-66IZ7Ox1CUYeorQptNRSuO2o3ZjETMuZEz6t4j0Y73fZcZrMJEH3W2DcLsJiW90FBkuO3aSyXUvYga9a4DcaMCNBEPWAdfCbSGWnviU_-G3xQj07tQavrS13DNLmVIdT6n_xJNcgLw53mY59fz7eNjLmidmB_vH8dP9JVnF0BeJaU3O9w?width=2785&height=1072&cropmode=none)

![image1](https://4ltnmw.dm.files.1drv.com/y4mFdpZT99VPwwCDNYanxPWBWunyqkFPrQjP79USuho-fuY7GvHZMWIdQ-6KIULEqYLul1axknGVS49qSSoN4KgzC7FshCOMn6Y5v78WT2tn3PIrzy7jMk9dJPxOeizAq6wVRXsuAWYTcuX7DQKzvxZNDigiGQimlRG_WNSfo3dyvbQkkVumjt4UIkDIKpKw6ZhF8j4EyqSIOkS9VTOv3epFA?width=2874&height=1245&cropmode=none)


