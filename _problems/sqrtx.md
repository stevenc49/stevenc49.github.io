---
layout: page
title:  Sqrt(x)
last_solved: 2020-07-24
category: Binary Search
leetcode_url: https://leetcode.com/problems/sqrtx
status: Attempted
---

Problem
-------

```
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

```

Solution
----------

Binary search, where if the (current value)^2 is greater than x, than it can't be in second half.

- [Terrible Whiteboard](https://www.youtube.com/watch?v=VYtEKhxKd1Q&feature=emb_logo)

My first attempt with memory limit exceeded.

{% highlight python %}

def mySqrt(self, x: int) -> int:
    
    nums = [i for i in range(x+1)]
    
    low, high = 0, len(nums)
    
    while low<=high:
        
        mid = (low+high)//2
        
        square = nums[mid]**2
        
        if square == x:
            print("found at %s" % mid)
            return mid
        elif square > x:  
            print(low, high)
            high = mid-1    # ignore right half
        else:
            print(low, high)
            low = mid+1     # ignore left half
    
    return high     # low and high will converge to [3] which is index 2

{% endhighlight %}

_________________

Without "number line array"


{% highlight python %}

def mySqrt(self, x: int) -> int:
            
    low, high = 0, x
    
    while low<=high:
        
        mid = (low+high)//2
        
        square = mid**2
        
        if square == x:
            print("found at %s" % mid)
            return mid
        elif square > x:  
            print(low, high)
            high = mid-1    # ignore right half
        else:
            print(low, high)
            low = mid+1     # ignore left half
    
    return high     # low and high will converge to [3] which is index 2

{% endhighlight %}

____________-

using powerful binary search template

{% highlight python %}

    def mySqrt(self, x: int) -> int:
               
        # 1 2 3 4    x=4 sqrt=16
        
        left, right = 0, x+1
        
        while left<right:
            
            mid = (left+right)//2
            
            square = mid*mid
            
            if square>x:   # condition is k**2 > x
                right = mid
            else:
                left = mid+1
            
        return left-1   # left is minimum k value satisfying condition, k-1 is answer
    
    
    # k^2 x=8 condition
    # 4^2>8   true   
    # 3^2>8   true    left is this k, the minimum k satisfying the condition
    # 2^2>8   false   the answer is this, so use left-1
    # 1^2>8   false

{% endhighlight %}

![image1]()