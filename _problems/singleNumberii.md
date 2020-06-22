---
layout: page
title:  Single Number II
last_solved: 2020-06-22
category: bit manipulation
leetcode_url: https://leetcode.com/problems/single-number-ii
status: Attempted
---

Problem
-------

```
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

```

Solution
----------

If a number appears 3 times, then its sum of bits will be of the form ```3 * n```.
But if it only appears once, then it's sum of bits will be ```n```.

So iterate thru all 32 bits of integers, adding their sums, mod it by 3 and the remaining will be the answer.

Let's take [2,2,3,2] for example.

```
0 1 0   | 2
0 1 0   | 2
0 1 0   | 2
1 0 0   | 3
---------------
1 3 0   sum of each digit column


1 % 3 => 1
3 % 3 => 0
0 % 0 => 0

The answer is 3
```

{% highlight python %}

{% endhighlight %}


![image1]()