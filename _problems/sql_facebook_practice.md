---
layout: page
title:  SQL Facebook Practice Questions
last_solved: 
category: sql
leetcode_url: 
status: Attempted
---

[sql fiddle](http://sqlfiddle.com/#!15/8a51c/1)

Problem
-------

{% highlight sql %}

create table salesperson (
   id int,
  name varchar,
  age int,
  salary int
);

create table customer (
  id int,
  name varchar,
  city varchar,
  industrytype varchar
  );
  
 create table orders (
   number int,
   order_date date,
   cust_id int,
   salesperson_id int,
   amount int
   );
   
insert into salesperson values (1, 'Abe', 61, 140000);
insert into salesperson values (2, 'Bob', 34, 44000);
insert into salesperson values (5, 'Chris', 34, 40000);
insert into salesperson values (7, 'Dan', 41, 52000);
insert into salesperson values (8, 'Ken', 57, 115000);
insert into salesperson values (11, 'Joe', 38, 38000);


insert into customer values (4, 'Samsonic', 'pleasant', 'J');
insert into customer values (6, 'Panusung', 'oaktown', 'J');
insert into customer values (7, 'Samony', 'jackson', 'B');
insert into customer values (9, 'Orange', 'jackson', 'B');


insert into orders values (10, '1996-8-2', 4, 2, 540);
insert into orders values (20, '1999-1-30', 4, 8, 1800);
insert into orders values (30, '1995-7-14', 9, 1, 460 );
insert into orders values (40, '1998-1-29', 7, 2, 2400 );
insert into orders values (50, '1998-2-3', 6, 7, 600 );
insert into orders values (60, '1998-3-2', 6, 7, 720 );
insert into orders values (70, '1992-5-6', 9, 7, 150 );



{% endhighlight %}

Solution
----------

{% highlight sql %}

-- a. The names of all salespeople that have an order with Samsonic. 
select name
from salesperson
where id in (
  select o.salesperson_id
  from orders o join customer c on o.cust_id=c.id
  where c.name='Samsonic'
)
 


-- b. The names of all salespeople that do not have any order with Samsonic. 
select distinct s.name
from orders o join salesperson s on o.salesperson_id=s.id
where cust_id not in (
  select id
  from customer
  where name='Samsonic'
)
  
-- c. The names of salespeople that have 2 or more orders. 
select name
from salesperson
where id in (
-- use group/having to get ids of salespeople with count>=2
select o.salesperson_id
from salesperson s join orders o on s.id=o.salesperson_id
group by o.salesperson_id
having count(*)>=2
 );
 
-- d. The names and ages of all salespersons must having a salary of 100,000 or greater.
select name, age
from salesperson
where salary>100000;



-- e. What sales people have sold more than 1400 total units?
select distinct s.name
from salesperson s join orders o on s.id=o.salesperson_id
where o.salesperson_id in
(
  select salesperson_id
  from orders
  group by salesperson_id
  having sum(amount) > 1400
 );


-- f. When was the earliest and latest order made to Samsonite?

select number
from orders
where cust_id=4  -- join and get customer name if you have to
and order_date in (
  
 -- earliest order
 select min(order_date)
 from orders o join customer c on c.id=o.cust_id
 where c.name='Samsonic'
 
 union
 
 -- latest order
  select max(order_date)
 from orders o join customer c on c.id=o.cust_id
 where c.name='Samsonic'
 )


{% endhighlight %}


![image1]()