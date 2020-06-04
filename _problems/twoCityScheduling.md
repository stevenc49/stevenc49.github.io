---
layout: page
title:  Two City Scheduling
last_solved: 2020-06-03
category: greedy
leetcode_url: https://leetcode.com/problems/two-city-scheduling
status: Attempted
---

Problem
-------

{% highlight text %}

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

{% endhighlight %}

Solution
----------

{% highlight python %}

costs = [
    [10,20],
    [30,200],
    [400,50],
    [30,20]
]

def minCosts(costs):

    n = len(costs)//2

    # calculate the difference between city A and city B for each person
    delta = [(a - b) for a, b in costs]
    print( "delta: ", delta )

    # get the ordered difference
    ordered_delta = sorted((value, i) for (i, value) in enumerate(delta))
    print( "ordered delta:", ordered_delta )
    
    minimum_cost = 0

    # for the n smallest cost_A - cost_B, it costs a lot to fly to B,
    # so we send them to city A
    print( "ordered_delta[:n] ", ordered_delta[:n] )
    for value, i in ordered_delta[:n]:
        minimum_cost += costs[i][0]

    # for the n greatest cost_A - cost_B, it costs a lot to fly to A,
    # so we send them to city B
    for value, i in ordered_delta[n:]:
        minimum_cost += costs[i][1]
    return minimum_cost

print( minCosts(costs) )

{% endhighlight %}

```
delta:  [-10, -170, 350, 10]
ordered delta: [(-170, 1), (-10, 0), (10, 3), (350, 2)]
ordered_delta[:n]  [(-170, 1), (-10, 0)]
110
```


![image1](https://gnfhha.dm.files.1drv.com/y4muHXtqyUxi04APXeMASIp-yHG57ZaQjRlTKOSEZKuTP093gr_IpctxKHrhcC_w5Dzj7GjGOia0S0fzqFCQEz4yVcm_3f0UP9NtsNzDCAU51qivDcj1tmMKDm1QAQNtdEOfxjQpmxE3uGQtsQRVjcwv5NX9dhqis6gkW1_MkABagijSZSmRh6Tpe5a3aMOtLvkGib3dWO9QvYuDPpBBgsDxA?width=2245&height=1049&cropmode=none)