---
layout: page
title:  Find all Duplicates in Array
last_solved: 2020-08-06
category: array
leetcode_url: https://leetcode.com/problems/find-all-duplicates-in-an-array
status: Attempted
---

Problem
-------

```
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

```

Solution
----------

If you can use extra space for a hashmap. Then you can use this one-liner

{% highlight python %}

def findDuplicates(self, nums: List[int]) -> List[int]:
    
    c = Counter(nums)
    
    print(c)
    
    # output = []
    # for k, v in c.items():
    #     if v==2:
    #         output.append(k)
    
    return [k for k,v in c.items() if v==2]

{% endhighlight %}


![image1]()