---
layout: page
title:  Longest Palindromic Substring
last_solved: 
category: 
leetcode_url: 
status: Attempted
---

Problem
-------

```
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

```

Solution
----------

This only works for both even and odd palindromes but TLE on "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"

{% highlight python %}

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def isPalindrome(s):
            return s==s[::-1]
        
        longestPalindrome=""
        
        for i in range(len(s)):
            
            l=i
            r=i
            
            while l>=0 and r<len(s):

                # odd case
                currPalindrome = s[l:r+1]
                if isPalindrome(currPalindrome):
                    if len(currPalindrome)>len(longestPalindrome):
                        longestPalindrome = currPalindrome
                
                # even case
                currPalindrome = s[l:r+2]
                if isPalindrome(currPalindrome):
                    if len(currPalindrome)>len(longestPalindrome):
                        longestPalindrome = currPalindrome
                
                l-=1
                r+=1
        
        print(isPalindrome("bab"))
        return longestPalindrome

{% endhighlight %}


![image1]()