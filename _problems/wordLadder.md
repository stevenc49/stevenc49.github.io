---
layout: page
title:  Word Ladder
last_solved: 2020-07-23
category: bfs
leetcode_url: https://leetcode.com/problems/word-ladder
status: Attempted
---

Problem
-------

```
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

```

Solution
----------

{% highlight python %}


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # preprocess first
# defaultdict(<class 'list'>,
#             {'c*': ['cog'],
#              'c*g': ['cog'],
#              'c*og': ['cog'],
#              'd*': ['dot', 'dog'],
#              'd*g': ['dog'],
#              'd*og': ['dog'],
#              'd*ot': ['dot'],
#              'd*t': ['dot'],
#              'h*': ['hot'],
#              'h*ot': ['hot'],
#              'h*t': ['hot'],
#              'l*': ['lot', 'log'],
#              'l*g': ['log'],
#              'l*og': ['log'],
#              'l*ot': ['lot'],
#              'l*t': ['lot']}
        
        
        
        L = len(beginWord)
        
        # make adjacency list
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # key is the generic word
                # value is a list of words which have the same intermediate generic word
                all_combo_dict[word[:1] + "*" + word[i+1:]].append(word)
        
        pp.pprint(all_combo_dict)

{% endhighlight %}


![image1]()