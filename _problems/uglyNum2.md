---
layout: page
title:  Ugly Num II
last_solved: Attempted
category: math
leetcode_url: https://leetcode.com/problems/ugly-number-ii
status: Attempted
---

Problem
-------

```
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

```

Solution
----------

Works for small cases but not large cases. TLE

{% highlight python %}

def nthUglyNumber(self, n: int) -> int:
    
    uglyNums = [1]
    
    curr = 2
    while len(uglyNums)<n:
        
        prevNum = curr
        
        # factorize
        if curr%5==0 and int(curr/5) in uglyNums:
            uglyNums.append(curr)
        elif curr%3==0 and int(curr/3) in uglyNums:
            uglyNums.append(curr)
        elif curr%2==0 and int(curr/2) in uglyNums:
            uglyNums.append(curr)

        curr+=1
    
    
    print(uglyNums)
    return uglyNums[-1]

{% endhighlight %}


![image1]()