---
layout: page
title:  Reverse Integer
last_solved: 2020-06-02
category: math
leetcode_url: https://leetcode.com/problems/reverse-integer
status: Attempted
---

##### Problem

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

##### Solution

{% highlight python %}

def reverse(self, num: int) -> int:
    
    # handle negative case
    neg = False
    if num<0:
        neg = True
        num = abs(num)

    rev = 0

    while num>0:

        # pop last digit
        popped = num % 10
        num = math.floor(num / 10)

        rev = rev * 10 + popped

        print(num, popped, rev)


    return rev*-1 if neg else rev

{% endhighlight %}

![image1]()