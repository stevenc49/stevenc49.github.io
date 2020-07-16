---
layout: page
title:  Pow(x, n)
last_solved: 2020-07-16
category: bit manipulation
leetcode_url: https://leetcode.com/problems/powx-n/
status: Attempted
---

Problem
-------

```
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

```

Solution
----------

Didn't quite get it to work. Do check out [Timonthy's explanation](https://www.youtube.com/watch?v=Twr5TD8Fvbo)


{% highlight python %}

def myPow(self, x: float, n: int) -> float:
    
    if n<0:
        x = 1/x
        n = n*-1
    
    output = 1
    while n>0:
        if n&1:
            print(n, x, output)
            output *= x
        n>>=1
        x=x*x
    return output

{% endhighlight %}


![image1]()