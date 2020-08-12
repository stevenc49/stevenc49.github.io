---
layout: page
title:  customers who never order
last_solved: 
category: sql
leetcode_url: https://leetcode.com/problems/customers-who-never-order/solution/
status: solved
---

Problem
-------

```
Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+


```

Solution
----------

method 1: not in - subquery

{% highlight sql %}

select name as 'Customers'
from Customers
where id not in 
(
    select customerid from orders
)


{% endhighlight %}

___________

left join and filter nulls

{% highlight sql %}

select c.name as 'Customers'
from Customers c left join Orders o
on c.id=o.customerid
where o.customerid is null


{% endhighlight %}

![image1]()