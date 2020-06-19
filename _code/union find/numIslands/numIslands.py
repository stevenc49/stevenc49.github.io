
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","1","0"]
]





def numIslands(grid):

    R = len(grid)
    C = len(grid[0])
    numIslands = 0

    def floodFill(grid, r,c):

        # Approach 1
        print(r,c,grid[r][c])

        if grid[r][c] == '1':   # this means we can advance
            grid[r][c] = '0'    # mark as visited
            if r>=1: floodFill(grid, r-1, c)
            if r+1<R: floodFill(grid, r+1, c)
            if c>=1: floodFill(grid, r, c-1)
            if c+1<C: floodFill(grid, r, c+1) 
    
        # Approach 2 - check out of bounds
        if r < 0 or r >=R or c < 0 or c >= C or grid[r][c] == "0":
            return 0
        else:
            print(r,c,grid[r][c])

            grid[r][c] = '0'    # mark as visited
            floodFill(grid, r-1, c)
            floodFill(grid, r+1, c)
            floodFill(grid, r, c-1)
            floodFill(grid, r, c+1) 

    
    for i in range(R):
        for j in range(C):
            if grid[i][j]=='1':
                numIslands+=1
                floodFill(grid, i, j)
    

    print(grid)
    return numIslands

print(numIslands(grid))