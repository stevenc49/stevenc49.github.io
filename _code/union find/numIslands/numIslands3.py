from itertools import product

grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","1"],
    ["0","0","0","1","0"]
]

def numIslands(grid):

    rows = len(grid)
    cols = len(grid[0])

    def dfs(i, j):

        if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]=="0":
            return

        neib_list = [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]
        for x, y in neib_list:
            grid[i][j]="0"
            dfs(x, y)

    count = 0
    for i, j in product(range(rows), range(cols)):
        if grid[i][j]=="1":
            count += 1
            dfs(i, j)

    return count
    
print( numIslands(grid) )