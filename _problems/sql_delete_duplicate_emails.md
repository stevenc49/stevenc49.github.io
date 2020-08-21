---
layout: page
title:  Delete Duplicate Emails
last_solved: 
category: sql
leetcode_url: https://leetcode.com/problems/delete-duplicate-emails
status: Attempted
---

Problem
-------

```
Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+

```

Solution
----------

For deletion, start with selection, then modify to deletion

{% highlight sql %}

select a.*
from person a join person b on a.email=b.email
where a.id > b.id

{% endhighlight %}

{% highlight sql %}

delete a
from person a join person b on a.email=b.email
where a.id > b.id

{% endhighlight %}


![image1]()