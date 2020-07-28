---
layout: page
title:  Find Min in Sorted Array
last_solved: 2020-07-27
category: 
leetcode_url: 
status: Attempted
---



Try a more concise solution:

{% highlight python %}

l, r = 0, len(nums)  - 1
while nums[l] > nums[r]:
    mid =  int((l+r)/2)  
    if nums[mid] >= nums[l]:
        l = mid + 1
    else:
        r = mid
return nums[l]

{% endhighlight %}


Think of examples with each of the if statements


if nums[mid] > nums[mid+1]:

mid = 1, nums=1
[2,1,3]




{% highlight python %}

arr = [4,5,6,7,2,3]

def findMin(nums):

    # 1-elem array
    if len(nums)==1:
        return nums[0]

    left = 0
    right = len(nums)-1

    # this condition means arr is already sorted, so just return first element
    if nums[right] > nums[0]:
        return nums[0]


    while right>=left:

        mid = left + (right-left) // 2

        # min found: case 1
        if nums[mid] > nums[mid+1]:     # 3 4 5 1 2 where 5 is mid
            return nums[mid+1]

        # min found: case 2
        if nums[mid-1] > nums[mid]:     # 4 5 1 2 3 where 1 is mid
            return nums[mid]


        ### min not found cases below
        # mid is greater than first elem so ignore left half
        if nums[mid] > nums[0]:
            left = mid+1

        # mid is less than first elem, ignore right half
        else:
            right = mid-1


print(findMin(arr))


{% endhighlight %}


