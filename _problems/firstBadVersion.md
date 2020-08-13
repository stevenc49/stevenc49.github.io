---
layout: page
title:  First Bad Version
last_solved: 
category: binary search
leetcode_url: https://leetcode.com/problems/first-bad-version
status: Attempted
---

Problem
-------

```
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

```

Solution
----------

Check for condition at mid and to the right of mid.

```

    |   |  
1 2 3 4 5
F F F T T

```

{% highlight python %}

def firstBadVersion(self, n):

    low, high = 1, n
    
    while low<=high:
        
        mid = (low+high)//2
        
        if isBadVersion(mid) and not isBadVersion(mid-1):
            return mid
        elif not isBadVersion(mid):
            low = mid+1
        else:
            high = mid-1
    
    return -1

{% endhighlight %}


________________


{% highlight python %}

def firstBadVersion(self, n):

    left, right = 1, n
    
    while left < right:
        
        mid = (left+right)//2
        
        if isBadVersion(mid):
            
            right = mid
            
        else:
            
            left = mid + 1
    
    return left

{% endhighlight %}

![image1]()