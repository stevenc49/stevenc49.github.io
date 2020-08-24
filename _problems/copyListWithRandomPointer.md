---
layout: page
title:  Copy List with Random Pointer
last_solved: 
category: 
leetcode_url: linked list
status: Attempted
---

Problem
-------

```
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
```

Solution
----------

It's trivial to clone the linked list but not with the random pointer.
The random pointer would point to a node that hasn't been cloned yet.

1) Go thru list and build a hashmap with K=original node and V=cloned node
2) Go thru the list again and wire up the `next` and `random` cloned nodes


This has a bug and haven't been able to figure it out.

{% highlight python %}

from collections import defaultdict

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        
        curr = head
        mapping = defaultdict(Node)
        
        # go thru list once and just create nodes and add to mapping
        while curr:
            
            # create new node
            newNode = Node(curr.val, None, None)
            
            # add to map
            mapping[curr] = newNode
            
            # move to next node
            curr = curr.next
        
        
        # go thru list again and wire up the next and random pointers
        curr = head
        
        while curr:
            
            # get cloned node
            clonedCurr = mapping[curr]
            
            # get next and random of original node
            origNext = curr.next
            origRandom = curr.random
            
            # get cloned version of orig next and random
            clonedNext = mapping.get(origNext, None)
            clonedRandom = mapping.get(origRandom, None)
            
            # print(clonedCurr.val)
            # print(clonedNext.val)
            # print()
            # print(clonedCurr.val, origNext.val, clonedNext.val)
            
            # wire up cloned nodes
            clonedCurr.next = clonedNext
            clonedCurr.next = clonedRandom
            
            
            # move to next node
            curr = curr.next
            
        
        return mapping[head]

{% endhighlight %}

______________



{% highlight python %}


{% endhighlight %}

![image1]()