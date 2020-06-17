---
layout: page
title:  House Robber
last_solved: 2020-06-16
category: dp
leetcode_url: https://leetcode.com/problems/house-robber
status: Solved
---

First few cases are trivial.

Starting from n>=3, it's the max of alternating sequences.


Gotcha:
- be careful when to use nums array and when to use dp array
- make sure to use a different dp array and don't overwrite the given `nums` array

{% highlight python %}

nums = [1,2,3,1]


def rob(nums):

    if not nums: return 0
    if len(nums)==1: return nums[0]
    
    dp = [1] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        # dp.append( max( nums[i] + dp[i-2], dp[i-1] ) )
        dp[i] = max( nums[i] + dp[i-2], dp[i-1] )


    return dp[-1]

print(rob(nums))

{% endhighlight %}

The dp array looks like ```[1, 2, 4, 4]```


![image1]()