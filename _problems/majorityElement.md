---
layout: page
title:  Majority Element
last_solved: 
category: boyer moore
leetcode_url: https://leetcode.com/problems/majority-element/
status: Attempted
---

Problem
-------

```
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
```

Solution
----------



{% highlight python %}

        count, cand = 0, None
        
        for n in nums:
            
            if count==0:
                cand=n
            
            if cand==n:
                count+=1
            else:
                count-=1
               

            
        return cand

{% endhighlight %}

______________



{% highlight python %}


{% endhighlight %}

![image1]()