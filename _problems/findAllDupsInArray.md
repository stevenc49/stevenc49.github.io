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

________________

To not use any additional space, we can only modify the existing array.
Use the constraint `1<a[i]<n`

- Map the current value to it's position in the array. (ie: [4,3,2,7,...], '7' is in the 4's place, so make 7->-7)
- If there is another 4 in the array, it will check the 7 and see that it's negative. If it's negative, add it to the output array.



{% highlight python %}

def findDuplicates(self, nums: List[int]) -> List[int]:
    
    # [4,3,2,7,8,2,3,1]
    # [2,2]
    
    output = []
    
    for i,v in enumerate(nums):           
        
        pos_v = abs(v)
        
        if nums[pos_v-1]<0:
            output.append(pos_v)
        
        # mark as visited
        nums[pos_v-1] = abs(nums[pos_v-1])*-1

{% endhighlight %}

________________

![image1]()