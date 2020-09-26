---
layout: page
title:  Generate Parenthesis
last_solved: 2020-08-18
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

n=3

def generateParenthesis(n):
    
    def backtrack(outputList, currentString, open, close, n):

        # base case
        if len(currentString)==2*n:
            outputList.append(currentString)
            print("output " + currentString)
            return

        print( currentString )

        # decisions below
        if open < n:
            backtrack( outputList, currentString+"(", open+1, close, n )

        if close < open:
            backtrack( outputList, currentString+")", open, close+1, n)
            
    outputList = []
    backtrack(  outputList, "", 0, 0, n)
    return outputList
        

print( generateParenthesis(n) )
    

{% endhighlight %}


```

(
((
(((
((()
((())
output ((()))
(()
(()(
(()()
output (()())
(())
(())(
output (())()
()
()(
()((
()(()
output ()(())
()()
()()(
output ()()()
['((()))', '(()())', '(())()', '()(())', '()()()']

```

![image1](https://i.ibb.co/Dr9xNgv/image.png)