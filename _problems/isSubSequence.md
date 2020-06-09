---
layout: page
title:  Is Subsequence
last_solved: 2020-07-08
category: strings, 2ptr
leetcode_url: https://leetcode.com/problems/is-subsequence
status: Attempted
---

Problem
-------

```
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

```

Solution
----------

Gotchas:
- 2 ptrs on string, have two conditions on while loop

{% highlight python %}

def isSubsequence(s, t):

    sp = 0
    tp = 0

    while sp<len(s) and tp<len(t):

        if s[sp]==t[tp]:
            sp+=1
            tp+=1
            continue
        else:
            tp+=1

    # reached end of s
    return sp==len(s)

{% endhighlight %}


![image1]()