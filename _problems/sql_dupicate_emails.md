---
layout: page
title:  Duplicate Emails
last_solved: 
category: sql
leetcode_url: https://leetcode.com/problems/duplicate-emails/
status: Attempted
---

Problem
-------

```
Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+

```

Solution
----------

{% highlight sql %}

select Email
from person
group by email
having count(*)>1

{% endhighlight %}


![image1]()