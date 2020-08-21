---
layout: page
title:  Number Complement
last_solved: 
category: binary
leetcode_url: https://leetcode.com/problems/number-complement
status: Attempted
---

Problem
-------

```
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

```

Solution
----------

Using binary string.

{% highlight python %}

    def findComplement(self, num: int) -> int:
        
        binString = bin(num).replace('0b', '')
            
        output = ''
        for c in binString:
            
            if c=='0':
                output+='1'
            else:
                output+='0'
        
        return int(output, 2)

{% endhighlight %}

______________

using bit manipulation

{% highlight python %}

    def findComplement(self, num: int) -> int:
        ## RC ##
		## APPROACH : BIT MANIPULATION ##
		## LOGIC ##
		#	1. 1 xor 1 = 0 and 0 or 1 = 1, from these we can say that XORing with 1 will give its complement bit
		#	2. so, for 5 ==> 101, bitmask is 111, for 6 ==> 110, bitmask is 111, so bitmask is (length number of 1's)
		#	3. How do we length of given bit ? we use log function
		#	4. (ex: for 5), we take 1 and left shift by length obtained from 3, i.e (1000) now, substract 1, it will give (111) ==> bitmask
		
        ## TIME COMPLEXICITY : O(1) ## (coz make n= 32)
		## SPACE COMPLEXICITY : O(1) ##
        
        n = floor(log2(num)) + 1        # n is a length of num in binary representation
        bitmask = (1 << n) - 1          # bitmask has the same length as num and contains only ones 1...1
        return bitmask ^ num

{% endhighlight %}

![image1]()