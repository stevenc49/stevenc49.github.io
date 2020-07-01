---
layout: page
title:  Arrange Coins
last_solved: 2020-07-01
category: binary search
leetcode_url: https://leetcode.com/problems/arranging-coins
status: Attempted
---

Problem
-------

```
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

```

Solution
----------

Tried the intuitive solution first but it ran into TLE.

It's actually a binary search question similar to [Search Insert Position](/problems/searchInsertPosition)

There's suppose to be a binary search solution to this but I don't get it. I"m just using the brute force solution.


```

1
2 3
4 5 6
7 8 9 10


so array would be like:
0 1 2 3 4 5 6 7 8 9 10
0 1 1 2 3 3 3 4 4 4 4 


```



{% highlight python %}

def arrangeCoins(self, n: int) -> int:
        
        curr = 0
        count = 0
        
        a = [0]*(n+1)
        
        for i in range(0, n+1):
            a[i] = curr
        
            print(curr, count)
        
            if curr!=count:
                count += 1
            else:
                curr += 1
                count = 0
        
        
        print(a)
        return a[n]

{% endhighlight %}

_________

Another solution that worked is from [Timonthy H Chang](https://www.youtube.com/watch?v=vPvnYNjqSh0)


{% highlight pyth        stairs, coins, i = 0,1,1
        
        while coins<=n:
            
            stairs +=1
            i+=1
            coins+=i
        
        return stairson %}

def arrangeCoins(self, n: int) -> int:
    
    stairs, coins, i = 0,1,1
    
    while coins<=n:
        
        stairs +=1
        i+=1
        coins+=i
    
    return stairs

{% endhighlight %}



![image1](https://5wk0dw.dm.files.1drv.com/y4mDOQ_Aow8T07qO5MeTglwEhC1FGZodPmP_3PEBa6wm4eaDUIDb7DosTOGVGDBxSiVFrVe7xxBuUfn804lAkQthVjHQODZoYhqM3Ahrf5d_h_ZU_ffSnDmqTAIBlKK-TVlq-VY-nDkOd1TZpRWjlqbsnbw9fxoQSiltW1MbXy4eTW9JIkzOmxIoglcZNJzns2ldLzMY0cLK3SDwxoxu85Upw?width=1401&height=1049&cropmode=none)

