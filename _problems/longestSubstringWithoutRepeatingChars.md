---
layout: page
title:  Longest Substring without Repeating Characters
---

{% highlight text %}

{% endhighlight %}


{% highlight python %}


s = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

def lengthOfLongestSubstring(s):

    start = 0
    end = 0
    maxRes = 0

    charSet = set()

    while end < len(s):

        if not s[end] in charSet:
           charSet.add(s[end])
           end+=1
           maxRes = max(len(charSet), maxRes)     # why max? of max
        else:
            charSet.remove(s[start])
            start+=1

    return maxRes


print(lengthOfLongestSubstring(s))      # 3 abc
print(lengthOfLongestSubstring(s2))     # 1 b
print(lengthOfLongestSubstring(s3))     # 3 wke


{% endhighlight %}


![image1]()