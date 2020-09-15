---
layout: page
title:  Combination Sum III
last_solved: 
category: backtrack
leetcode_url: https://leetcode.com/problems/combination-sum-iii
status: Attempted
---

Problem
-------

```
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

The solution set must not contain duplicate combinations.
 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Example 3:

Input: k = 4, n = 1
Output: []
Example 4:

Input: k = 3, n = 2
Output: []
Example 5:

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
```

Solution
----------



{% highlight python %}

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        
        output = []
        
        def backtrack(output, current, num, sumsofar):
            
            if len(current)==k and sumsofar==n:
                output.append(current.copy())
                return
            
            for i in range(num, 10):
                if sumsofar+1 > n: break
                backtrack(output, current+[i], i+1, sumsofar+i)
                
        
        
        backtrack(output, [], 1, 0)
        return output
    

{% endhighlight %}

______________



{% highlight python %}


{% endhighlight %}

![image1]()