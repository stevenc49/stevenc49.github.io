---
layout: page
title:  Sort Colors
last_solved: 2020-08-04
category: arrays, sorting
leetcode_url: https://leetcode.com/problems/sort-colors/
status: Solved
---

Problem
-------

```
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

```

Solution
----------

{% highlight python %}

nums = [2,0,2,1,1,0]

def sortColors(nums):
    
    start = 0
    end = len(nums)-1
    index = 0
    
    # 2 0 2 1 1 0    i=0    s=0    e=5
    # 0 0 2 1 1 2    i=1    s=0    e=4
    
    while index<=end and start<end:
        
        if nums[index]==0:
            nums[start]=0
            nums[index]=nums[start]
            start+=1
            index+=1
        
        elif nums[index]==2:
            nums[index]=nums[end]
            nums[end]=2
            end-=1
            #index+=1
        
        else:
            index+=1
    
        print(nums, index, start, end)
    
    return nums


print( sortColors(nums) )

{% endhighlight %}



-----------------

{% highlight python %}

def sortColors(self, nums: List[int]) -> None:

    start = 0
    end = len(nums)-1
    index = 0
    
    def swap(nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    
    while start<end and index<=end:
        
        if nums[index]==0:
            swap(nums, start, index)
            start+=1
            index+=1
        elif nums[index]==2:
            swap(nums, index, end)
            end-=1
        else:
            index+=1
        
{% endhighlight %}


-----------------

{% highlight python %}

def sortColors(self, nums: List[int]) -> None:

    s = 0
    e = len(nums)-1
    p = 0
    
    def swap(nums,x,y):
        tmp = nums[x]
        nums[x] = nums[y]
        nums[y] = tmp
    
    while p<=e:
        
        if nums[p]==2:
            swap(nums, p, e)
            e-=1
        elif nums[p]==0:
            swap(nums, p, s)
            s+=1
            p+=1
        else:
            p+=1
    
    return nums
        
{% endhighlight %}


![image1]()