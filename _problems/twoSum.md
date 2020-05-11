---
layout: page
title:  Two Sum
---

### Description

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

{% highlight text %}

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

{% endhighlight %}

### Solution

{% highlight python %}

nums = [2, 7, 11, 15]
target = 26


def twoSum(nums, target):

    length = len(nums)
    for i in range(0, length):
        for j in range(i+1, length):

            if nums[i] + nums[j] == target:

                return (i, j)
                break

            j=j+1


res = twoSum(nums, target)
print res


{% endhighlight %}




