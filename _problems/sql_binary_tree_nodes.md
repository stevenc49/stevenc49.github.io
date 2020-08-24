---
layout: page
title:  SQL Binary Tree Nodes
last_solved: 
category: sql
leetcode_url: https://www.hackerrank.com/challenges/binary-search-tree-1
status: Attempted
---

Problem
-------

```
You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.



Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

Root: If node is root node.
Leaf: If node is leaf node.
Inner: If node is neither root nor leaf node.
Sample Input



Sample Output

1 Leaf
2 Inner
3 Leaf
5 Root
6 Leaf
8 Inner
9 Leaf

Explanation

The Binary Tree below illustrates the sample:

```

Solution
----------

{% highlight sql %}

select n,
case 
    when p is null then 'Root'
    -- case when n not in (2,6,4,15,9,13,11) then 'Leaf' else 'Inner'
    when n in (select distinct p from bst) then 'Inner'
    else 'Leaf'
    end

end
from bst
order by n;

{% endhighlight %}


![image1]()