---
layout: page
title:  Reverse String
last_solved: 2020-06-01
category: string
leetcode_url: https://leetcode.com/problems/reverse-string/
status: Solved
---

##### Problem

{% highlight text %}

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

{% endhighlight %}

##### Solution

{% highlight python %}

def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    
    if not s: return
    
    start = 0
    end = len(s)-1
    
    while start<end:
        
        tmp = s[start]
        s[start] = s[end]
        s[end] = tmp
        
        start+=1
        end-=1
    


{% endhighlight %}


![image1]()