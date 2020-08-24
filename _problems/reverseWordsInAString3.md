---
layout: page
title:  Reverse Words in a String III
last_solved: 
category: string
leetcode_url: https://leetcode.com/problems/reverse-words-in-a-string-iii/
status: Solved
---

Problem
-------

```
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
```

Solution
----------

Some things to note:
- can't do swaps on string characters, need to convert to list first
- string.extend() takes content of list and appends it to another list


{% highlight python %}

    def reverseWords(self, s: str) -> str:
        
        letters = list(s)   
        
        def reverse(letters, startIndex, endIndex):
            
            left, right = 0, endIndex
            
            while left<right:
                
                # can't do item assignments on strings, therefore need to turn to list first (like toCharArray() in java)
                letters[left], letters[right] = letters[right], letters[left]   
            
                left+=1
                right-=1
            
            return letters
        
        
        tokens = s.split(" ")
        
        output = []
        for token in tokens:
            
            reversed = reverse(list(token), 0, len(token)-1)
            output.extend(reversed)     # extend extracts contents from list and appends to other list
            output.extend([" "])
        
        output = output[:-1]        # remove last space value
        
        print(output)
        
        return "".join( output )

{% endhighlight %}

______________



{% highlight python %}


{% endhighlight %}

![image1]()