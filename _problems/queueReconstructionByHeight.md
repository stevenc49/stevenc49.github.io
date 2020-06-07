---
layout: page
title:  Queue Reconstruction By Height
last_solved: 2020-06-06
category: greedy
leetcode_url: https://leetcode.com/problems/queue-reconstruction-by-height/
status: Attempted
---

Problem
-------

```

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

```

Solution
----------

{% highlight python %}

def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    
    print(people)

    # sort ppl by decending height first and k second
    people.sort(key=lambda x: (-x[0], x[1]))

    print(people)

    ans = []
    for person, num in people:

        if num >= len(ans):
            ans.append([person, num])
        else:
            ans.insert(num, [person, num])
    return ans

{% endhighlight %}

After the initial sort, it looks like this:
```
[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
[[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
```


![image1]()