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

This solution doesn't handle overflows yet. Check out [this](https://www.youtube.com/watch?v=ThdOYKsFSK0) video: 

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

        # handle overflow
        if (rev > 2**31 / 10) or (rev == 2**31 / 10 and popped>7): return 0
        if (rev < -2**31 / 10) or (rev == -2**31 / 10 and popped<-8): return 0

        rev = rev * 10 + popped
    
        print(num, popped, rev)


    return rev*-1 if neg else rev

{% endhighlight %}


```2**31 = 2147483648```
```-2**31 = -2147483648```

This is what happens when it overflows

{% highlight text %}
153423646 9 9
15342364 6 96
1534236 4 964
153423 6 9646
15342 3 96463
1534 2 964632
153 4 9646324
15 3 96463243
1 5 964632435
0 1 9646324351
9646324351
{% endhighlight %}

This is what happens when we prevent the overflow
{% highlight text %}
153423646 9 9
15342364 6 96
1534236 4 964
153423 6 9646
15342 3 96463
1534 2 964632
153 4 9646324
15 3 96463243
1 5 964632435
0
{% endhighlight %}

![image1]()