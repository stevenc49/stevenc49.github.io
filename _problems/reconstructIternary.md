---
layout: page
title:  Template
last_solved: 
category: 
leetcode_url: 
status: Attempted
---

Problem
-------

```
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.


```



Solution
----------

Solution that I came up with myself. It works for the first test case but doesn't handle the lexical duplicate tickets.

{% highlight python %}

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

def findTicketIndForStartCity(startCity):

    # TODO: store all ticket indexes that have the same start city
    sameStartCityIndex = {}

    for ticketInd, cities in enumerate(tickets):
        if cities[0]==startCity:
            return ticketInd


output = ['JFK']
for i in range(0, len(tickets)):

    currTicketIndex = findTicketIndForStartCity( output[-1] )
    nextCity = tickets[currTicketIndex][1]
    output.append(nextCity)

print(output)

{% endhighlight %}


![image1]()