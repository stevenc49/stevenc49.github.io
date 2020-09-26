---
layout: page
title:  Valid Parenthesis
last_solved: 
category: stack
leetcode_url: https://leetcode.com/problems/valid-parentheses
status: Attempted
---

Problem
-------

```
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
```

Solution
----------



{% highlight python %}

    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for c in s:
            if c=='(':
                stack.append(')')
            elif c=='[':
                stack.append(']')
            elif c=='{':
                stack.append('}')
            elif not stack or stack.pop()!=c:
                return False
        
        return not stack

{% endhighlight %}

______________



{% highlight python %}


{% endhighlight %}

![image1]()