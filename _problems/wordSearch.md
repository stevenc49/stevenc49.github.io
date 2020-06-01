---
layout: page
title:  Word Search
last_solved: 2020-06-01
category: matrix
leetcode_url: https://leetcode.com/problems/word-search/
status: Attempted
---

##### Problem

{% highlight text %}

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

{% endhighlight %}

##### Solution

tep is to prevent going back

{% highlight python %}


        R = len(board)
        C = len(board[0])

        def searchWord(i, j, word, index):

          if index==len(word):
            return True

          if i<0 or i>=R or j<0 or j>=C or board[i][j]!=word[index]:
            return False

          tmp = board[i][j]
          board[i][j] = ' '
          # found = searchWord(i+1,j,word,index+1)
          found = searchWord(i-1,j,word,index+1) or \
            searchWord(i+1,j,word,index+1) or \
            searchWord(i,j-1,word,index+1) or \
            searchWord(i,j+1,word,index + 1)

          board[i][j] = tmp
          return found

        for i in range(R):
          for j in range(C):
            if board[i][j]==word[0] and searchWord(i,j,word,0):
              return True

        return False

{% endhighlight %}


![image1]()