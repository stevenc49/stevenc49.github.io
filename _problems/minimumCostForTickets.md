---
layout: page
title:  Minimum Cost For Tickets
last_solved: 
category: dp
leetcode_url: https://leetcode.com/problems/minimum-cost-for-tickets/
status: Attempted
---

Problem
-------

```
In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
```

Solution
----------



{% highlight python %}

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        last_day = days[-1]
        dp = [0] * (last_day + 1) 
        days = set(days) # convert day to set for fast look up later
        for d in range(1, last_day + 1):
            # to make sure we have pass, we either buy a 1-d pass today, a 7-d pass 6 days ago, or a 30-d pass 29 days ago
            if d in days:
                dp[d] = min(costs[2] + dp[max(d - 30, 0)],
                            costs[1] + dp[max(d - 7, 0)],
                            costs[0] + dp[d - 1])
            else: # we don't buy pass on day not in days
                dp[d] = dp[d - 1]
                
        print(days)
        return dp[-1]

{% endhighlight %}

______________



```
Your input
[1,4,6,7,8,20]
[2,7,15]
stdout
{1, 4, 6, 7, 8, 20}

Output
11
Expected
11
```

![image1]()