---
layout: page
title:  SQL - Second Highest Salary (limit/offset + ifnull)
last_solved: 
category: sql
leetcode_url: https://leetcode.com/problems/second-highest-salary
status: Attempted
---

Problem
-------

```
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

```

Solution
----------

Normally something like this is sufficient if you just use the limit and offset clause.

{% highlight sql %}

select distinct salary as SecondHighestSalary
    from employee
    order by salary desc
    limit 1 offset 1

{% endhighlight %}

Without limit, the resultset is
```
300
200
100
```

- offset chooses the one you want and puts it on the top
- limit just selects the top one

But we also have to use the ifnull( if this is null , return this value ) clause

{% highlight sql %}

select ifnull(

    (select distinct salary as SecondHighestSalary
    from employee
    order by salary desc
    limit 1 offset 1)
    
,  
    null 
) as SecondHighestSalary 

{% endhighlight %}




![image1]()