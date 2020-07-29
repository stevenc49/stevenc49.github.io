---
layout: page
title:  Convert Sorted Array to Binary Search Tree
last_solved: 
category: 
leetcode_url: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
status: Attempted
---

Problem
-------

```
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

```

Solution
----------

{% highlight python %}

def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    
    def buildTree(nums, left, right):
        
        if left>right: return
        
        mid = (left+right) // 2
        
        node = TreeNode(nums[mid])
        
        node.left = buildTree(nums, left, mid-1)
        node.right = buildTree(nums, mid+1, right)
        
        return node
    
    if not nums: return None
    
    return buildTree(nums, 0, len(nums)-1)

{% endhighlight %}


![image1]()