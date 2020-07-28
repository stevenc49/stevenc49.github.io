---
layout: page
title:  Most Common Word
last_solved: 
category: heap
leetcode_url: https://leetcode.com/problems/most-common-word
status: Attempted
---

Problem
-------

```
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

 

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

```

Solution
----------

{% highlight python %}

def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    
#         # tokens = paragraph.split()
#         tokens re.split(', | .', paragraph)
#         print(tokens)
    
#         words = []
#         for word in tokens:
#             # words.append( word.lower().strip(',') )
#             words.append( re.sub('[^A-Za-z0-9]+', '', word.lower()) )
    
#         print(words)
    
    #1). replace the punctuations with spaces,
    #      and put all letters in lower case
    normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

    #2). split the string into words
    words = normalized_str.split()

    c = Counter(words)
    print(c)
    
    # set banned words to zero
    for k,v in c.items():
        if k in banned:
            c[k] = 0
    
    # turn counter into a list
    c = [(-v,k) for k,v in c.items()]
    print(c)
    
    heapq.heapify(c)
    return heapq.heappop(c)[1]

{% endhighlight %}


![image1]()