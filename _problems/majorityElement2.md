---
layout: page
title:  Majority Element II
last_solved: 
category: boyer moore
leetcode_url: https://leetcode.com/problems/majority-element-ii
status: Attempted
---

Problem
-------

```

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
```

Solution
----------



{% highlight python %}

        count1, count2, cand1, cand2 = 0,0,None, None
        
        for n in nums:
            
            if cand1==n:
                count1+=1
            elif cand2==n:
                count2+=1
            elif count1==0:
                cand1=n
                count1+=1
            elif count2==0:
                cand2=n
                count2+=1
            else:
                count1-=1
                count2-=1
        
        
        print( count1, count2, cand1, cand2)
        
        # 2nd pass
        result = []
        for c in [cand1, cand2]:
            if nums.count(c) > len(nums)//3:
                result.append(c)


        return result
        


{% endhighlight %}

______________



{% highlight python %}


{% endhighlight %}

![image1]()