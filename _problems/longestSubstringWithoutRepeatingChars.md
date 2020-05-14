---
layout: page
title:  Longest Substring without Repeating Characters
---




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

        print(s[start], s[end], charSet, maxRes)

        if not s[end] in charSet:
           charSet.add(s[end])
           end+=1
           maxRes = max(len(charSet), maxRes)     # why max? of max
        else:
            charSet.remove(s[start])
            start+=1

    return maxRes


print(lengthOfLongestSubstring(s))      # 3 abc
# print(lengthOfLongestSubstring(s2))     # 1 b
# print(lengthOfLongestSubstring(s3))     # 3 wke

{% endhighlight %}

Time Complexity O(2n) = O(n), where i and j will visit each char twice (see printout section)
Space O(min(size of n, size of charset))


#### Printouts


{% highlight text %}

For s = "abcabcbb"
print(s[start], s[end], charSet, maxRes)

a a set() 0
a b {'a'} 1
a c {'b', 'a'} 2
a a {'b', 'c', 'a'} 3
b a {'b', 'c'} 3
b b {'b', 'c', 'a'} 3
c b {'c', 'a'} 3
c c {'b', 'c', 'a'} 3
a c {'b', 'a'} 3
a b {'b', 'c', 'a'} 3
b b {'b', 'c'} 3
c b {'c'} 3
c b {'b', 'c'} 3
b b {'b'} 3
b b set() 3
3

{% endhighlight %}


#### Dry Run


{% highlight text %}



s="abcabcbb"


iter=1
    s[start]=a
    s[end]=a

    a not in charSet
    charSet = {a}
    maxRes = max(1, 0) = 1

iter=2
    start=a, end=b

    charSet = {a,b}
    maxRes = max(2, 1) =2

iter=3
    start=a, end=c

    charSet = {a,b,c}
    maxRes = max(3, 2)

iter=4
    start=a, end=a

    charSet.remove('a') -> charSet={b,c}
    maxres = 3 (still 3 from last iteration)

iter=5
    a<bca>bcbb

    charSEt={b,c}
    end=b in charSet -> charSEt.remove(c) -> charSEt={c}
    maxres = max(1, oldMaxres), max(1,3) = 3    <- this is why we have maxres=max(len,oldMaxres)
    start+=1

iter=6
    ab<cab>cbb

    start=c, end=b
    end=b not in charSEt -> charSEt={b,c}

{% endhighlight %}


![image1]()