---
layout: page
title: Maximum Product Subarray
---




#### Solution

One pass, keep track of minCurrent and maxCurrent

{% highlight python %}

arr1 = [2, 3, -2,4]
arr2 = [2, 3, 6]
arr3 = [2, -3, 6]

def getMaxProductSubarray(nums):
    if not nums: return
    left, right, record = 0, 0, -float('inf')
    for i in range(len(nums)):
        left = (left or 1) * nums[i]
        right = (right or 1) * nums[-i-1]
        record = max(record, left, right)
    return record

def getMaxProductSubarray(arr):

    minCurrent = 1
    maxCurrent = 1
    maxRes = -99999

    for i in range(len(arr)):

        current = arr[i]

        print(i, current, minCurrent, maxCurrent)

        if current>0:
            maxCurrent = maxCurrent * current
            minCurrent = min( minCurrent * current, 1)
        elif current==0:
            maxCurrent=1
            minCurrent=1
        else:
            x = maxCurrent
            maxCurrent = max( minCurrent * current, 1)
            minCurrent = x * current
        
        print(i, current, minCurrent, maxCurrent)

        if maxRes<maxCurrent:
            maxRes = maxCurrent
        
    return maxRes


print(arr1)
print(getMaxProductSubarray(arr1))
print()

print(arr2)
print(getMaxProductSubarray(arr2))
print()

print(arr3)
print(getMaxProductSubarray(arr3))
print()


{% endhighlight %}


{% highlight text %}

[2, 3, -2, 4]
0 2 1 1
0 2 1 2
1 3 1 2
1 3 1 6
2 -2 1 6
2 -2 -12 1
3 4 -12 1
3 4 -48 4
6

[2, 3, 6]
0 2 1 1
0 2 1 2
1 3 1 2
1 3 1 6
2 6 1 6
2 6 1 36
36

[2, -3, 6]
0 2 1 1
0 2 1 2
1 -3 1 2
1 -3 -6 1
2 6 -6 1
2 6 -36 6
6

{% endhighlight %}