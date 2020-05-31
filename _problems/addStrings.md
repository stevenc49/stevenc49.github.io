---
layout: page
title:  Add Strings
last_solved: 2020-05-30
category: math
leetcode_url: https://leetcode.com/problems/add-strings/
status: [ Attempted ]
---

##### Problem

Given "12" and "3", return "15".
Write your own itoa and atoi



##### Solution

{% highlight python %}

def addStrings(self, num1: str, num2: str) -> str:
    
    
    def itoa(num1):
        
        sum=0
        digitCol = 0
        for i in reversed( range(len(num1)) ):
            
            digit = ord(num1[i])-ord('0')   # '2'-'0' = 2
            sum += (digit * (10**digitCol))
            digitCol+=1
        
        return(sum)
    
    return itoa(num1)+itoa(num2)

{% endhighlight %}


![image1]()