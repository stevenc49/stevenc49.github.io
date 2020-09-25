---
layout: page
title:  Minimum Add to Make Parentheses Valid
last_solved: 
category: stack
leetcode_url: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
status: Attempted
---

Problem
-------

```
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0
Example 4:

Input: "()))(("
Output: 4
```

Solution
----------



{% highlight python %}

    def minAddToMakeValid(self, S: str) -> int:
        
        numInvalid = 0
        stack = []
        
        for c in S:
            
            if c=="(":
                stack.append(1)
            
            elif c==")":
                
                if not stack:
                    numInvalid+=1
                else:
                    stack.pop()
                
        return numInvalid + len(stack)

{% endhighlight %}

______________

Some other solutions

{% highlight python %}


  numInvalid=0
  stack=[]
  
  for c in text:
    if c=='(':
      stack.append(c)
      numInvalid+=1
      
    elif c==')':
      if not stack:
        numInvalid+=1
      else:
        stack.pop()
        numInvalid-=1
    
  return numInvalid 

'''''''''''''''''''''''''

res = 0
stack = 0
  for bracket in text:
    if bracket == '(':
      stack += 1
    if bracket == ')' and stack != 0:
      stack -= 1
    elif bracket == ')' and stack == 0:
      res += 1
  return res + stack
  

{% endhighlight %}

![image1]()