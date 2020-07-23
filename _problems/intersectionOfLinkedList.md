---
layout: page
title:  Intersection of Two Linked Lists
last_solved: 2020-07-22
category: linked list
leetcode_url: https://leetcode.com/problems/intersection-of-two-linked-lists/
status: Attempted
---

Problem
-------

```
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 

Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.

```

Solution
----------

- Solution 1: O(MN) solution, iterate thru every node in list A, check to see if it's in list B
- Solution 2: Use hashmap and store reference
- Solution 3: This is a trick to do it in O(n), you just have to know it.
    - Iterate listA and listB at the same time, when listA ends, move it to listB's head (and vice versa)
    - Where they meet is the intersection
- Solution 4: Find length difference
    - Iterate Both list and get lengths
    - Find the difference between the lengths
    - The intersection is at the length difference

{% highlight python %}

# Solution 3: Iterate and move to alternate list when at the end
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    
    if not headA or not headB: return None
    
    listAhead = headA
    listBhead = headB
    
    while headA is not headB:
        
        # if there's no cycles, both pointers will eventually get to each other's end of list
        if headA.next is None and headB.next is None:
            return None
        
        # transverse A
        if headA.next:
            headA = headA.next
        else:
            headA = listBhead
        
        # transverse B
        if headB.next:
            headB = headB.next
        else:
            headB = listAhead
    
    return headA

{% endhighlight %}


![image1]()