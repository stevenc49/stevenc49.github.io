---
layout: page
title:  nth digit
last_solved: 
category: math
leetcode_url: https://leetcode.com/problems/nth-digit/
status: Attempted
---

Problem
-------

```
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

```

Solution
----------

Do not understand logic yet. Learn from [this discussion](https://leetcode.com/problems/nth-digit/discuss/88369/0ms-C%2B%2B-Solution-with-Detail-Explanation)

{% highlight python %}

    def findNthDigit(self, n: int) -> int:
        
        # https://leetcode.com/problems/nth-digit/discuss/88369/0ms-C%2B%2B-Solution-with-Detail-Explanation
        
        # 1) find out how many digits the number has (n=250, digits=3)
        base=9
        digits=1
        while n-base*digits > 0:
            n-=base*digits
            base*=10
            digits+=1
            print(n, base, digits)
            
        # 2) calc what the number is
        index = (n-1) % digits
        offset = (n-1) / digits
        start = pow(10, digits-1)
        
        print(index, offset, start)
        return str(int(start+offset))[index]

{% endhighlight %}


![image1]()