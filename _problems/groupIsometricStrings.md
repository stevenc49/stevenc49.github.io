---
layout: page
title:  Group Isometric Strings
last_solved: 2020-06-11
category: hashmap
leetcode_url: https://leetcode.com/discuss/interview-question/368038/Amazon-or-Onsite-or-Group-Isomorphic-Strings
status: Solved
---

Problem
-------

Two strings are isomorphic if each character of their strings can be mapped to another character and retain the same "structure".

`egg` and `add` are isomorphic
`e->a, g->d`

```
Given: [“foo”, “bar”, “paper”, “title”, “egg”, “add”]
Expected: [[“bar”],[“paper” “title”], [“egg”, “add”, "foo”]]

```

Solution
----------

{% highlight python %}

def normalize(word):
    
    # print("in normalize")
    # print(word)
    
    res = ""
    count = 0
    
    map = {}
    for c in word:
        if c not in map:
            map[c] = count
            count+=1
        else:
            res += str(map[c])
    
    return res

def findIso(arr):
    
    map = {}
    
    # first pass to build map
    for word in arr:
        if normalize(word) not in map:
            map[ normalize(word) ] = [word]
        else:
            existingList = map[ normalize(word) ]
            existingList.append(word)
            map[ normalize(word) ] = existingList
    
    
    # second pass to extract grouped words in the map
    result = []
    for groupedWords in map.values():
        result.append( groupedWords )
    
    return result

input1 = ["foo", "bar", "paper", "title", "egg", "add"]
res = findIso(input1)
print(res)

{% endhighlight %}


![image1]()