---
layout: page
title:  Num Ones
---


#### Loop and Bit Mask

{% highlight python %}

    def hammingWeight(self, n: int) -> int:
        
        count = 0
        while n>0:
            
            if n&1==1:
                count+=1
            
            n>>=1
        
        return count
        

{% endhighlight %}


![image1]()