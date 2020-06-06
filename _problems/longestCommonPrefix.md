---
layout: page
title:  Longest Common Prefix
last_solved: 2020-06-05
category: string
leetcode_url: https://leetcode.com/problems/longest-common-prefix
status: Solved
---

Problem
-------

```
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

```

Solution
----------

{% highlight python %}

def lcp(strs):

    prefix = strs[0]

    for i in range(1, len(strs)):

        # if substring is found, it will return the first index
        # if that element isn't the first char, then chop off
        while strs[i].find(prefix) != 0:

            # keep chopping off the last character
            prefix = prefix[0: len(prefix)-1]
            if not prefix: return ""
        
    return prefix

{% endhighlight %}


![image1]()