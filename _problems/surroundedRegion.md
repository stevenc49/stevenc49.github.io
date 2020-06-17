---
layout: page
title:  Surrounded Region
last_solved: 2020-06-16
category: union find
leetcode_url: https://leetcode.com/problems/surrounded-regions
status: Attempted
---

Problem
-------

```
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

```

Solution
----------

We need to have some way to figure out which cells are "surrounded" by X. If they are surrounded, we don't flip them. To do this:

- First, go thru border cells and run DFS on them, temporarily turning them to another color 'T'.
- Then run DFS on inner cells, turning O to X
- Lastly, rerun DFS on border cells, turning 'T' back to 'X'



{% highlight python %}

from itertools import product

'''
	https://leetcode.com/problems/surrounded-regions/discuss/691646/Python-O(mn)-3-colors-dfs-explained
'''

board = [
	["X","X","X","X"],
	["X","O","O","X"],
	["X","X","O","X"],
	["X","O","X","X"]
]


class Solution:

    def dfs(self, i, j):
        
        if i<0 or j<0 or i>=self.M or j>=self.N or self.board[i][j] != "O":
            return
        self.board[i][j] = 'T'
        neib_list = [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]
        for x, y in neib_list:
            self.dfs(x, y)
    
    def solve(self, board):
        if not board: return 0
        self.board, self.M, self.N = board, len(board), len(board[0])
        
        for i in range(0, self.M):
            self.dfs(i,0)
            self.dfs(i,self.N-1)
            
        for j in range(0, self.N):
            self.dfs(0,j)
            self.dfs(self.M-1,j)
        
        for i,j in product(range(self.M), range(self.N)):
            board[i][j] = "X" if board[i][j] != "T" else "O"

sol = Solution()
sol.solve(board)

print(board)

{% endhighlight %}


![image1]()