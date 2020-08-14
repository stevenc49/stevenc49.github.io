---
layout: page
title:  Longest Palindromic Substring
last_solved: 
category: string, palindrome
leetcode_url: 
status: Solved
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

This only works for both even and odd palindromes but TLE on "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb...."

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

_______________

Same as approach above (Expand around center) but without the isPalindrome() method. 
I think that's what is causing it to time out.

{% highlight python %}

def longestPalindrome(self, s: str) -> str:
    
    # return the actual palindrome
    def expandAroundCenter(s, l, r):

        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1

        return s[l+1:r]



    res = ""
    for i in range(len(s)):
        oddPalin = expandAroundCenter(s, i, i)
        evenPalin = expandAroundCenter(s, i, i+1)

        if len(oddPalin)>len(res):
            res = oddPalin
        if len(evenPalin)>len(res):
            res = evenPalin

    return res

{% endhighlight %}

![image1]()