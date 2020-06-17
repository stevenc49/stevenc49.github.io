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
        
        # run dfs on sides
        for i in range(0, self.M):
            self.dfs(i,0)           # left side
            self.dfs(i,self.N-1)    # right side
        
        # run dfs on top and bottom
        for j in range(0, self.N):
            self.dfs(0,j)           # top
            self.dfs(self.M-1,j)    # bottom
        
        print(board)

        # itertools.product() is equivalent to nested forloop
        for i,j in product(range(self.M), range(self.N)):
            board[i][j] = "X" if board[i][j] != "T" else "O"

sol = Solution()
sol.solve(board)

print(board)