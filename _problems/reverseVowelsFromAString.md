---
layout: page
title:  Reverse Vowels Of a String
last_solved: 
category: string
leetcode_url: https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/
status: Attempted
---

Problem
-------

```
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

```

Solution
----------

Note:

- cannot swap characters in a string directly so change it to a list first and join them at the end

{% highlight python %}

def reverseVowels(self, s: str) -> str:
    
    lst = list(s)
    
    def isVowel(c):
        if c in "AEIOUaeiou":
            return True
        return False
    
    def swap(x,y,lst):
        tmp = lst[x]
        lst[x]=s[y]
        lst[y]=tmp
    
    
    left, right = 0, len(lst)-1
    
    
    while left<right:
        
        # get left to vowel
        while not isVowel(lst[left]) and left<right:
            left+=1
        
        # get right to vowel
        while not isVowel(s[right]) and left<right:
            right-=1
        
        # swap
        swap(left, right, lst)
        
        # move pointers
        left+=1
        right-=1
    
    return ''.join(lst)

{% endhighlight %}


![image1]()