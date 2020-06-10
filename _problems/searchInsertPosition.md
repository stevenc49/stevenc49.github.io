---
layout: page
title:  Search Insert Position
last_solved: 2020-06-10
category: binary search
leetcode_url: https://leetcode.com/problems/search-insert-position
status: Solved
---

Problem
-------

```
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

```

Solution
----------

{% highlight python %}

def searchInsert(nums, target):

    left = 0
    right = len(nums)-1

    while left<=right:

        mid = (left+right)//2

        if target==nums[mid]:
            return mid

        # left and right beside each other
        elif right-left<=1:

            # and target is inbetween (ie: [4,6], tar=5)
            if target>=nums[left] and target<=nums[right]:
                return left+1

            # target is outside of array (to the right)
            elif target>nums[right]:
                return right+1
            
            # target is outside of array (to the left)
            elif target<nums[left]:
                return left

        elif target>nums[mid]:
            left = mid+1
        elif target<nums[mid]:
            right = mid-1

    return -1



print( searchInsert( [1,3,5,6] , 5) )   # 2
print( searchInsert( [1,3,4,6] , 5) )   # 3
print( searchInsert( [1,2] , 3) )   # 2
print( searchInsert( [1,2] , 0) )   # 0
print( searchInsert( [1,3] , 2) )   # 1

{% endhighlight %}


Could've been more concise if you just returned left when none is found:

{% highlight python %}

def searchInsert(nums, target):

    left = 0
    right = len(nums)-1

    while left<=right:

        mid = (left+right)//2

        if target==nums[mid]:
            return mid

        # # left and right beside each other
        # elif right-left<=1:

        #     # and target is inbetween (ie: [4,6], tar=5)
        #     if target>=nums[left] and target<=nums[right]:
        #         return left+1

        #     # target is outside of array (to the right)
        #     elif target>nums[right]:
        #         return right+1
            
        #     # target is outside of array (to the left)
        #     elif target<nums[left]:
        #         return left

        elif target>nums[mid]:
            left = mid+1
        elif target<nums[mid]:
            right = mid-1

    return left

{% endhighlight %}



![image1]()