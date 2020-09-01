---
layout: page
title:  Tempalte
last_solved: 
category: 
leetcode_url: 
status: Attempted
---

Problem
-------

```
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

Solution
----------



{% highlight python %}

class MinStack:

    def __init__(self):

        self.stack = []
        

    def push(self, x: int) -> None:
        
        if not self.stack:
            minSoFar = x
        else:
            
            prevMin = self.stack[-1][1]
            minSoFar = min(prevMin, x)
            
        item = (x, minSoFar)
        self.stack.append( item )
        

    def pop(self) -> None:
        
        if self.stack:
            item = self.stack.pop()
            return item[0]
        

    def top(self) -> int:
        
        if self.stack:
            item = self.stack[-1]
            return item[0]

    def getMin(self) -> int:
        
        if self.stack:
            item = self.stack[-1]
            return item[1]

{% endhighlight %}

______________



{% highlight python %}


{% endhighlight %}

![image1]()