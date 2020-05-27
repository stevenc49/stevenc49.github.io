---
layout: page
title: Maximum Subarray
---




#### Naive Solution

nested forloop and sliding window



#### Dynamic programming solution (also known as kadane's algorithm)

runs in O(n) time

Gotcha:
- remember if i==0: continue, since if arr=[1], we just return 1

{% highlight python %}

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maxSubarray(arr):

    if not arr:
        return None

    for i in range(len(arr)):

        if i==0:
            continue
        else:
            # max of "start with this elem" or "continue the existing subarray"
            arr[i] = max(arr[i], arr[i-1] + arr[i])     
    
    
    return max(arr)

print(maxSubarray(arr))     # returns 6


{% endhighlight %}