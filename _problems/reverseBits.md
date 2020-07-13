---
layout: page
title:  Reverse Bits
last_solved: Solved
category: Bits
leetcode_url: https://leetcode.com/problems/reverse-bits
status: Solved
---

Problem
-------

```
Reverse bits of a given 32 bits unsigned integer.

 

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

```

Solution
----------

Try doing it by hand for a small test case like a number with 4 bits (see image).

{% highlight python %}

def reverseBits(self, n: int) -> int:
    
    output, power = 0, 31
    
    while n:
        output += (n&1) << power
        n>>=1
        power-=1
    
    return output

{% endhighlight %}


![image1](https://5wizmw.dm.files.1drv.com/y4mU0kKdlap0lTnvFuIlluTwIYshPYaprTkHKJLryfgid6p0j5D9rNwGI7j-QbfbVWZin0j6QstrypxExk0g8t9rrKpBL1XGemV7OLVw9nyJNcbPI-5Cn_NNqTSR4UEfUe5uMePXSkTkz8QC0IuOl8WS1vyNMj6c9nHVv4daJn7TKBtZ5L4g5LtyU1oMP0jz42RO9FcIhcIexp0jaazW9F4Wg?width=2710&height=1085&cropmode=none)