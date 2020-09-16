---
layout: page
title:  Maximum XOR of Two Numbers in an Array
last_solved: 
category: bits
leetcode_url: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
status: Attempted
---

Problem
-------

```
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
```

Solution
----------



{% highlight python %}

    def findMaximumXOR(self, nums: List[int]) -> int:
        
        output, mask = 0,0
        
        for i in range(4,-1,-1):
            
            mask = mask | (1<<i)
            
            print(bin(mask))
            
            
            found = set([n&mask for n in nums])
            print(found)
            
            temp = output | 1 << i
            for f in found:
                if f^temp in found:
                    output = temp
        
        return output


{% endhighlight %}

______________



```

Your input
[3, 10, 5, 25, 2, 8]

stdout
0b10000
{0, 16}
0b11000
{0, 8, 24}
0b11100
{0, 8, 4, 24}
0b11110
{2, 4, 8, 10, 24}
0b11111
{2, 3, 5, 8, 10, 25}

Output
28

```

![image1]()