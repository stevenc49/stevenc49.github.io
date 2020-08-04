---
layout: page
title:  Power of Four
last_solved: 
category: bit manipulation
leetcode_url: https://leetcode.com/problems/power-of-four/
status: Attempted
---

Problem
-------

```
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

```

Solution
----------

{% highlight python %}

def isPowerOfFour(self, num: int) -> bool:
    
    numOnes = 0
    numZerosBeforeOne = 0
    
    while num>0:
        
        if num&1:
            numOnes+=1
        else:
            numZerosBeforeOne+=1
        
        num>>=1
    
    if numOnes==1 and numZerosBeforeOne%2==0:
        return True
    else:
        return False
            

{% endhighlight %}


![image1]()