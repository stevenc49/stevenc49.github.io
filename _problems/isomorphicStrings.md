---
layout: page
title:  Isomorphic Strings
last_solved: 2020-08-04
category: hashmap
leetcode_url: https://leetcode.com/problems/isomorphic-strings
status: Solved
---

Problem
-------

```
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

```

Solution
----------

{% highlight python %}

def isIsomorphic(self, s: str, t: str) -> bool:

    """
        egg -> 011
        add -> 011
    """
    def isohash(word):
        
        mapping = defaultdict(int)  # key=character, value=seqNum
        res = ""
        seqNum = 0   # seqNum is number that was assigned to char, for "egg": e is assigned '1', g is assigned '2'

        """
            mapping[e]=1
            mapping[g]=2
        """
        for c in word:
            if c not in mapping:
                mapping[c] = seqNum         # assign a number to char (keep track of it in hashmap)
                seqNum+=1                   # increment seqNum by 1 for the next character
                res += str(mapping[c])      # add seqNum to res
            else:
                res += str(mapping[c])      # if already assigned, just add to res
    

        return res
    
    
    return isohash(s)==isohash(t)

{% endhighlight %}


![image1]()