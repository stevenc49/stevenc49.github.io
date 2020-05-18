---
layout: page
title:  Missing Number
---

#### sort


#### hashset



#### gauss equation

{% highlight python %}

def missingNumber(self, nums: List[int]) -> int:
    
    n=len(nums)
    expected = (n*(n+1))//2
    actual = sum(nums)
    return expected-actual

{% endhighlight %}

#### xor


{% highlight python %}

nums = [3,0,1]
 
n = len(nums)
 
# xor index with value
xor = 0
for i, num in enumerate(nums):
    xor ^= i^num
 
# xor with length gives you missing num
missing = xor^n
 
print(missing)

{% endhighlight %}


![image1](https://bubblesortblog.files.wordpress.com/2020/04/img_20200409_102858.jpg)