---
layout: page
title:  Implement Trie
last_solved: 2020-06-30
category: Attempted
leetcode_url: https://leetcode.com/problems/implement-trie-prefix-tree/
status: Attempted
---

Problem
-------

```
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

```

Solution
----------

This code doesn't work correctly. Need to check it and debug it.

[source](https://www.youtube.com/watch?v=KX2GdDZPxQA)

{% highlight python %}

class Node:
    def __init__(self):
        self.children = {}  # the children that this node points to
        self.endofword = False

class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        ptr = self.root

        for letter in word:

            if letter not in ptr.children:
                ptr.children[letter] = Node()

            # traverse down the tree
            ptr = ptr.children[letter]
        ptr.endofword = True

        

    def search(self, word: str) -> bool:

        ptr = self.root

        for letter in word:

            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]

        # check end of word?
        if ptr.endofword:
            return True
        else:
            return False



        

    def startsWith(self, prefix: str) -> bool:

        ptr = self.root

        for letter in prefix:

            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]

        return True




trie = Trie();

output = []
output.append( trie.insert("apple") )
output.append( trie.search("apple") )
output.append( trie.search("app") )
output.append( trie.startsWith("app") )
output.append( trie.insert("app") ) 
output.append( trie.search("app") )

print(output)

{% endhighlight %}


![image1]()