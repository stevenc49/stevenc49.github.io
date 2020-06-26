---
layout: page
title:  Generate Parenthesis
last_solved: 2020-06-25
category: backtracking
leetcode_url: https://leetcode.com/problems/generate-parentheses/
status: Attempted
---

Problem
-------

```
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

```

Solution
----------

For backtracking problems, think of the base case and decisions. Then follow the backtracking template.

base case is when current string == n*2 because when () is a pair.
the decision is when to put the open and close braces.


{% highlight python %}

def generateParenthesis(self, n: int) -> List[str]:
    
    def backtrack(outputList, currentString, open, close, max):
        
        # base case
        if len(currentString)==max*2:
            outputList.append( currentString )
            return
        
        #decisions below
        if open < max:
            backtrack( outputList, currentString+"(", open+1, close, max )
        
        if close < open:
            backtrack( outputList, currentString+")", open, close+1, max )
    
    outputList = []
    backtrack( outputList, "", 0, 0, n)
    return outputList
    

{% endhighlight %}


![image1]()