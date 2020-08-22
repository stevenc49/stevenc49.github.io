---
layout: page
title:  Triangles (SQL Case Statements)
last_solved: 
category: sql
leetcode_url: https://www.hackerrank.com/challenges/what-type-of-triangle/problem
status: Attempted
---

Problem
-------

```
Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

Equilateral: It's a triangle with  sides of equal length.
Isosceles: It's a triangle with  sides of equal length.
Scalene: It's a triangle with  sides of differing lengths.
Not A Triangle: The given values of A, B, and C don't form a triangle.
Input Format

The TRIANGLES table is described as follows:



Each row in the table denotes the lengths of each of a triangle's three sides.

Sample Input



Sample Output

Isosceles
Equilateral
Scalene
Not A Triangle
Explanation

Values in the tuple  form an Isosceles triangle, because .
Values in the tuple  form an Equilateral triangle, because . Values in the tuple  form a Scalene triangle, because .
Values in the tuple  cannot form a triangle because the combined value of sides  and  is not larger than that of side .

```

Solution
----------

{% highlight sql %}

select A,B,C,

case when A=B and B=C and C=A then 'Equilateral'
     when A=B or B=C or C=A then 'Isosceles'
     when A!=B and B!=C and C!=A and (A+B>C and B+C>A and A+C>A) then 'Scalene'
else 'Not A Triangle'
end

from triangles

{% endhighlight %}

___________

This is the right answer (just take away the A,B,C)

{% highlight sql %}

select A,B,C,

case when A+B>C and B+C>A and A+C>A then

    case when A=B and B=C and C=A then 'Equilateral'
         when A=B or B=C or C=A then 'Isosceles'
         else 'Scalene'
         end
         
else 'Not A Triangle'
end

from triangles

{% endhighlight %}


![image1]()