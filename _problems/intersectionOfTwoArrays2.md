---
layout: page
title:  Intersection of Two Arrays II
last_solved: 2020-06-05
category: array
leetcode_url: https://leetcode.com/problems/intersection-of-two-arrays-ii
status: Solved
---

Problem
-------

```
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

```

Solution
----------

### Sort Solution

TODO

### HashMap Solution

{% highlight python %}

def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
    map = {}
    for num in nums1:
        if num not in map:
            map[num] = 1
        else:
            map[num] = map[num] + 1

    # iter thru num2, if exist in map, minus it
    res = []
    for num in nums2:
        if num in map:
            res.append(num)
            if map[num]>1:
                map[num] = map[num]-1
            else:
                map.pop(num)

    return res

{% endhighlight %}


![image1]()