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