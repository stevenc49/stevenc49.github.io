---
layout: page
title:  First Unque Char in String
last_solved: 2020-06-06
category: string
leetcode_url: https://leetcode.com/problems/first-unique-character-in-a-string
status: Solved
---

Problem
-------

```
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

```

Solution
----------

{% highlight python %}

def firstUniqChar(self, s: str) -> int:
    
    if not s: return -1
    
    dict = {}
    
    # add to dict
    for c in s:
        if c not in dict.keys():
            dict[c] = 1
        else:
            dict[c] = dict[c]+1
    
    # find first char with count=1 and return it
    for i, c in enumerate(s):
        if dict[c]==1:
            return i
    
    return -1

{% endhighlight %}


![image1]()