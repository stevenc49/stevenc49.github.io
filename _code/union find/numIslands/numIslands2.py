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
        else:
            grid[i][j]="0"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

    count = 0
    for i in range(rows):
        for j in range(cols):

            if grid[i][j]=="1":
                count += 1
                dfs(i, j)

    return count
    
print( numIslands(grid) )