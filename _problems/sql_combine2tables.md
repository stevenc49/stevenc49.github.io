---
layout: page
title:  combine 2 tables
last_solved: 
category: sql
leetcode_url: https://leetcode.com/problems/combine-two-tables/
status: solved
---

Problem
-------

```
SQL Schema
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
 

Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:

FirstName, LastName, City, State

```

Solution
----------

{% highlight sql %}

# Write your MySQL query statement below

# select p.firstname, p.lastname, a.city, a.state
# from person p, address a
# where p.personid=a.addressid  # this is inner join


select p.firstname, p.lastname, a.city, a.state
from person p left join address a
on p.personid=a.personid

{% endhighlight %}


![image1]()