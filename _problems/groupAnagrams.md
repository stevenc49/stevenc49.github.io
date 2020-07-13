---
layout: page
title:  Group Anagrams
last_solved: 2020-07-13
category: hashmap
leetcode_url: https://leetcode.com/problems/group-anagrams/
status: Solved
---

Problem
-------

```
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

```

Solution
----------

My solution:

{% highlight python %}

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
    def sortWord(word):
        return ''.join(sorted(word))
    
    mapping = {}
    for word in strs:
        
        print(word)
        
        if sortWord(word) not in mapping:
            mapping[sortWord(word)] = [word]
        else:
            mapping[sortWord(word)] = mapping[sortWord(word)] + [word]
            
            # mapping[sortWord(word)] = mapping[sortWord(word)].append(word)
            
    print(mapping)
    
    return list(mapping.values())
    

{% endhighlight %}


_________



Timonthy's More Concise Solution. Using defaultdict() so you don't have to do "if value not in" code.

{% highlight python %}

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    def sortWord(word):
        return ''.join(sorted(word))

    lookup = defaultdict(list)

    for word in strs:
        lookup[ sortWord(word) ].append( word )

    return list(lookup.values())

{% endhighlight %}

![image1]()