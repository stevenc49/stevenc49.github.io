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

I did not solve this myself yet. Just got it from solutions tab and tried to analyse it.

{% highlight python %}

def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    
        # {'*og': ['dog', 'log', 'cog'],
        #  '*ot': ['hot', 'dot', 'lot'],
        #  'c*g': ['cog'],
        #  'co*': ['cog'],
        #  'd*g': ['dog'],
        #  'd*t': ['dot'],
        #  'do*': ['dot', 'dog'],
        #  'h*t': ['hot'],
        #  'ho*': ['hot'],
        #  'l*g': ['log'],
        #  'l*t': ['lot'],
        #  'lo*': ['lot', 'log']})
    
    
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0
    
    L = len(beginWord)
    
    # make adjacency list
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            # key is the generic word
            # value is a list of words which have the same intermediate generic word
            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
    
    #pp.pprint(all_combo_dict)
    
    # Queue for BFS
    queue = collections.deque([(beginWord, 1)])     # (word, level)
    
    # Visited to make sure we don't repeat processing same word.
    visited = {beginWord: True}
    
    while queue:
        current_word, level = queue.popleft()
        
        for i in range(L):
            
            # intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            
            # next states are all the words which share the same intermediate state
            for word in all_combo_dict[intermediate_word]:
                
                if word==endWord:
                    return level+1
                
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level+1) )
            
        all_combo_dict[intermediate_word] = []
        
    return 0

{% endhighlight %}


![image1]()