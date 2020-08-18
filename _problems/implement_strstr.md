---
layout: page
title:  Implement strstr
last_solved: 
category: string
leetcode_url: https://leetcode.com/problems/implement-strstr
status: Attempted
---

Problem
-------

```
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

```

Solution
----------

{% highlight python %}

    def strStr(self, haystack: str, needle: str) -> int:
        
        # "hello" "ll"
        
        if not needle: return 0
        
        for i in range(len(haystack)):
            
            if haystack[i]==needle[0]:
                
                substr = haystack[i:i+len(needle)]
                
                if substr==needle:
                    
                    return i
        
        
        return -1
    

{% endhighlight %}


![image1]()