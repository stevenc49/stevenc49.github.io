---
layout: page
title:  department highest salary
last_solved: 
category: sql
leetcode_url: https://leetcode.com/problems/department-highest-salary/
status: solved
---

Problem
-------

```
The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, your SQL query should return the following rows (order of rows does not matter).

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
Explanation:

Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.
```

Solution
----------


- First, just make the inner query to get departmentid and highest salary.

{% highlight sql %}

# get highest salary per department group
select departmentid, max(salary)
from employee
group by departmentid

{% endhighlight %}


It will look like:

```
deptid  | max(salary)
1       | 90000
2       | 80000
```

Then join tables and do a `where ... in` with results from inner query.

{% highlight sql %}

select d.name as 'Department', e.name as 'Employee', e.salary as 'Salary'
from Employee e join Department d on e.departmentid=d.id
where (e.departmentid, salary) in 
(
    # get highest salary per department group
    select departmentid, max(salary)
    from employee
    group by departmentid
)


{% endhighlight %}


![image1]()