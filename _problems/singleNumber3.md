---
layout: page
title:  Single Number III
last_solved: 2020-07-23
category: bit manipulation
leetcode_url: https://leetcode.com/problems/single-number-iii
status: Attempted
---

Problem
-------

```

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
```

Solution
----------

Solution 1: you could always add it to a hashmap or set and if the count==1, add it to the result

{% highlight python %}

counter = Counter(nums)

ans = []
for k,v in counter.items():
    if v==1:
        ans.append(k)

return ans

{% endhighlight %}


Solution 2 uses bit manipulation:

There's two tricks you need to be aware of.

- xor by itself cancels/zeros itself out (you know this already)
- to find the last bit set:
    - `firstbit = xor & (xor-1) ^ xor`
- xor is:
    - `a^b=c, a^c=b, b^c=a`

The code and explaination are [here](https://www.youtube.com/watch?v=B7rhKt77fbw)

{% highlight python %}

def singleNumber(self, nums: List[int]) -> List[int]:
    
    xor = 0
    for n in nums:
        xor ^= n
        
    # xor = num1 ^ num2
    firstbit = xor & (xor-1) ^ xor
    num1 = 0
    for n in nums:
        if n & firstbit:
            num1 ^= n
            
    return [num1, num1^xor]

{% endhighlight %}

![image1]()