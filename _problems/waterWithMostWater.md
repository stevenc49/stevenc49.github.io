---
layout: page
title:  Water with Most Water
last_solved: 2020-08-04
category: array, 2ptr
leetcode_url: https://leetcode.com/problems/container-with-most-water/
status: Solved
---



##### Problem

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

![water](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)



#### Solution

Since the area is limited to the shorter of the two lines, use 2 pointers and move the closer one inwards.


{% highlight python %}

def maxArea(height):

    left = 0
    right = len(height)-1

    maxArea = 0

    while left<right:

        minHeight = min( height[left], height[right] )
        distance = right-left

        maxArea = max( maxArea, minHeight*distance )

        # move shorter one inward
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    
    return maxArea

{% endhighlight %}


__________________-



{% highlight python %}

def maxArea(self, height: List[int]) -> int:
    
    s = 0
    e = len(height)-1
    
    maxArea = 0
    
    while s<e:
        
        area = (e-s) * min(height[s], height[e])
        
        if area>maxArea:
            maxArea = area
        
        if height[s]>height[e]:
            e-=1
        else:
            s+=1
        
    return maxArea

{% endhighlight %}

