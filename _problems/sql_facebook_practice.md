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

{% endhighlight %}


![image1]()