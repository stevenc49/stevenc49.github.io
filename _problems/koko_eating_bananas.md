---
layout: page
title:  Koko Eating Bananas
last_solved: 
category: binary search
leetcode_url: https://leetcode.com/problems/koko-eating-bananas
status: Attempted
---

Problem
-------

```
Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.

 

Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], H = 6
Output: 23
```

Solution
----------

Itiotion from [this video](https://leetcode.com/problems/koko-eating-bananas/)

Code from [powerful binary search template](https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems)

{% highlight python %}

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        
        def feasible(speed):  # mid is like "eating speed"
            
            total = 0
            for pile in piles:
                div = pile // speed
                if pile % speed != 0:
                    div +=1
                total += div
            
            return total <= H
            
        
        left, right = 1, max(piles)
        
        while left < right:
            
            mid = (left + right) // 2   # mid is like "eating speed"
            
            if feasible(mid):
                right = mid     # it's feasible but we want to find the smallest k, so ignore right side
            else:
                left = mid + 1
        
        return left

{% endhighlight %}

______________



{% highlight python %}


{% endhighlight %}

![image1]()