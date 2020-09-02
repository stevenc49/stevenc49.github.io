---
layout: page
title:  Reformat Department table (if and case statements)
last_solved: 
category: sql
leetcode_url: https://leetcode.com/problems/reformat-department-table/
status: Attempted
---

Problem
-------

```
Table: Department

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| revenue       | int     |
| month         | varchar |
+---------------+---------+
(id, month) is the primary key of this table.
The table has information about the revenue of each department per month.
The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].
 

Write an SQL query to reformat the table such that there is a department id column and a revenue column for each month.

The query result format is in the following example:

Department table:
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+

Result table:
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+

Note that the result table has 13 columns (1 for the department id + 12 for the months).

```

Solution
----------

Using MySQL if statement

`if ( condition , return_value_if_true , return_value_if_false )`

{% highlight sql %}

select 
    id,
    sum( if(month = 'Jan', revenue, null) ) as "Jan_Revenue",
    sum( if(month = 'Feb', revenue, null) ) as "Feb_Revenue",
    sum( if(month = 'Mar', revenue, null) ) as "Mar_Revenue",
    sum( if(month = 'Apr', revenue, null) ) as "Apr_Revenue",
    sum( if(month = 'May', revenue, null) ) as "May_Revenue",
    sum( if(month = 'Jun', revenue, null) ) as "Jun_Revenue",
    sum( if(month = 'Jul', revenue, null) ) as "Jul_Revenue",
    sum( if(month = 'Aug', revenue, null) ) as "Aug_Revenue",
    sum( if(month = 'Sep', revenue, null) ) as "Sep_Revenue",
    sum( if(month = 'Oct', revenue, null) ) as "Oct_Revenue",
    sum( if(month = 'Nov', revenue, null) ) as "Nov_Revenue",
    sum( if(month = 'Dec', revenue, null) ) as "Dec_Revenue"
    from Department
    group by id

{% endhighlight %}

Using Case Statement

`case when condition then ret_val_if_true else ret_val_if_false end`

{% highlight sql %}

select 

    id, 
    sum(case when month='Jan' then revenue else null end) as 'Jan_Revenue',
    sum(case when month='Feb' then revenue else null end) as 'Feb_Revenue',
    sum(case when month='Mar' then revenue else null end) as 'Mar_Revenue',
    sum(case when month='Apr' then revenue else null end) as 'Apr_Revenue',
    sum(case when month='May' then revenue else null end) as 'May_Revenue',
    sum(case when month='Jun' then revenue else null end) as 'Jun_Revenue',
    sum(case when month='Jul' then revenue else null end) as 'Jul_Revenue',
    sum(case when month='Aug' then revenue else null end) as 'Aug_Revenue',
    sum(case when month='Sep' then revenue else null end) as 'Sep_Revenue',
    sum(case when month='Oct' then revenue else null end) as 'Oct_Revenue',
    sum(case when month='Nov' then revenue else null end) as 'Nov_Revenue',
    sum(case when month='Dec' then revenue else null end) as 'Dec_Revenue'

from department
group by id


{% endhighlight %}

Note: if you don't have the `sum()`, the result will look like this and your Jan_Rev will be

`[1, 8000, 7000, 6000, null, null, null, null, null, null, null, null, null]`

or

```
+----+-------------+-------------+
| id | Jan_Revenue | Feb_Revenue |
+----+-------------+-------------+
|  1 |        NULL |        7000 |
|  1 |        8000 |        NULL |
|  1 |        NULL |        NULL |
|  2 |        9000 |        NULL |
|  3 |        NULL |       10000 |
+----+-------------+-------------+
```

- So that's why you need to `sum()` or `max()` as an aggregate to "merge them all".
- [This is why we need either SUM (NULL+8000+NULL) or MAX, in both cases 8000 will be used. Actually from MySQL version 5.7.5 you would get an error if you didn't use an aggregation method:](https://leetcode.com/problems/reformat-department-table/discuss/376357/MySQLPostgreSQL-solutions/471453)

```

{"headers": ["id", "Jan_Revenue", "Feb_Revenue", "Mar_Revenue", "Apr_Revenue", "May_Revenue", "Jun_Revenue", "Jul_Revenue", "Aug_Revenue", "Sep_Revenue", "Oct_Revenue", "Nov_Revenue", "Dec_Revenue"], "values": [[1, 8000, 7000, 6000, null, null, null, null, null, null, null, null, null], [2, 9000, null, null, null, null, null, null, null, null, null, null, null], [3, null, 10000, null, null, null, null, null, null, null, null, null, null]]}
```



![image1]()