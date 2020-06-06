---
layout: page
title:  Plus One
last_solved: 2020-06-05
category: array
leetcode_url: https://leetcode.com/problems/plus-one/
status: Solved
---

Problem
-------

```
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

```

Solution
----------

{% highlight python %}

def plusOne(self, digits: List[int]) -> List[int]:
    
    ptr = len(digits)-1
    carry = 1   # just set carry=1 to do get into the loop

    while carry==1:

        # edge case when carry=1 and ptr goes left off the edge (ie: '9')
        if ptr<0:
            digits.insert(0, 1)
            return digits

        # normal case: just add one to last digit
        if digits[ptr]>=0 and digits[ptr]<9:
            digits[ptr] = digits[ptr]+1
            carry=0
            return digits

        # edge case, set carry and move left
        elif digits[ptr]==9:
            digits[ptr] = 0
            carry = 1
            ptr-=1

    return digits

{% endhighlight %}


![image1]()