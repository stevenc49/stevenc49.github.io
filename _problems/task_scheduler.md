---
layout: page
title:  Task Scheduler
last_solved: 
category: heap, greedy
leetcode_url: https://leetcode.com/problems/task-scheduler/
status: Attempted
---

Problem
-------

```
You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

```

Solution
----------

[timothy h chang](https://www.youtube.com/watch?v=wTUsb3nuOCQ)

{% highlight python %}

def leastInterval(self, tasks: List[str], n: int) -> int:
    
    output, h = 0, []
    
    c = Counter(tasks)
    for k,v in c.items():
        heapq.heappush(h, (-v, k))  # (numTimes, char)  # the neg is for Max heap
    
    while h:
        i, temp = 0, []
        
        while i<=n:
            
            output +=1
            if h:
                nums,key = heapq.heappop(h)
                nums +=1
                if nums<0: temp.append((nums,key))
            if not h and not temp: break
            i+=1
        
        for k,v in temp:
            heapq.heappush(h,(k,v))
    
    return output
    
    print(h)

{% endhighlight %}


![image1]()