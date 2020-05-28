---
layout: page
title:  House Robber 2
---


Do house robber twice with a helper function. First time exclude first element, second exclude last element. Then take max.

Handle corner cases first.




{% highlight python %}

def rob(nums):

    # handle edge cases
    if not nums: return 0
    if len(nums)==1: return nums[0]
    if len(nums)==2: return max(nums[0], nums[1])

    def robHelper(nums):

        dp = [1] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max( nums[i] + dp[i-2], dp[i-1] )

        print(dp)

        return dp[-1]

    excludeFirst = nums[1:]
    excludeLast = nums[:-1]

    return max( robHelper(excludeFirst), robHelper(excludeLast)  )

{% endhighlight %}


![image1]()