---
layout: page
title:  Contains Duplicates
---

#### Sorting solution

Sort then check if consecutive numbers are increasing.
O(1) space, O(nlogn) time




#### HashTable/Set Solution

O(n) time, O(n) space

{% highlight python %}

def containsDuplicate(self, nums: List[int]) -> bool:
    
    set = {}
    for num in nums:
        if num in set:
            return True
        else:
            set[num] = None
    
    return False

{% endhighlight %}


#### Check len(set)==len(list)

{% highlight python %}

def containsDuplicate(self, nums: List[int]) -> bool:
    
    return len(set(nums))!=len(nums)

{% endhighlight %}

![image1]()