---
layout: page
title:  Buy and Sell Stock
last_solved: 2020-06-02
category: array
leetcode_url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
status: Solved
---

### Naive O(n^2) way


{% highlight python %}

def maxProfit(self, arr: List[int]) -> int:

    if not arr or len(arr)==0:
        return 0

    maxProfit = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j]-arr[i]>maxProfit:
                maxProfit = arr[j]-arr[i]

    return maxProfit

{% endhighlight %}

This takes too long if the input is [999, 998, 997, ...etc]



### 1 pass solution

{% highlight python %}

    def maxProfit(self, prices):
        
        # keep track of 2 variables
        minPrice = 99999
        maxProfit = 0
        
        # in each iteration, one of two things happen
        for i in range(0, len(prices)):
            
            # this if condition gets triggered if a new minPrice is detected
            if prices[i] < minPrice:
                minPrice = prices[i]
            
            # this if condition gets triggered if the current value's GAP from the minPrice is more than the maxProfit
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
            
        return maxProfit

{% endhighlight %}

Try it with [2,1,6,-8]

- i=0: minPrice set to 2 (first condition)
- i=1: minPrice set to 1 (first condition)
- i=2: 6-1 is the gap, and it replaces the maxProfit of 0
- i=3: first condition is triggered but it doesn't matter, maxProfit is returned