---
layout: page
title:  Ransom Note
last_solved: 
category: string
leetcode_url: https://leetcode.com/problems/ransom-note
status: Attempted
---

Problem
-------

```
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

```

Solution
----------

{% highlight python %}

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        letterCounts = Counter(magazine)
        
        print(letterCounts)
        
        for  c in ransomNote:
            
            if c in letterCounts and letterCounts[c]>0:
                letterCounts[c]-=1
                print(letterCounts)
                
            else:
                return False
        
        return True

{% endhighlight %}


![image1]()