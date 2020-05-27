---
layout: page
title:  Water with Most Water
---

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


![image1]()