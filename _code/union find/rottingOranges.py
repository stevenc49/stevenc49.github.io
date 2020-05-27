grid = [[2,1,1],[1,1,0],[0,1,1]]



def orangesRotting(grid):

    R = len(grid)
    C = len(grid[0])

    fresh_count=0

    # get all cells with rotton oranges
    rottonQueue = []
    for i in range(R):
        for j in range(C):
            if grid[i][j]==2:
                rottonQueue.append( (i,j) )
            elif grid[i][j]==1:
                fresh_count+=1

    minutes_passed = 0

    while rottonQueue and fresh_count>0:

        minutes_passed+=1

        # process orange at the current level
        for i in range(len(rottonQueue)):

            # get rotton
            x, y = rottonQueue.pop(0)

            # visit neighbours
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:

                # calculate coordinates of adjacent cells
                xx, yy = x+dx, y+dy

                # ignore cell if it's out of boundary
                if xx<0 or xx==R or yy<0 or yy==C:
                    continue

                # ignore cell if it is empty '0' or visited before '2'
                if grid[xx][yy]==0 or grid[xx][yy]==2:
                    continue
                
                # update fresh count
                fresh_count-=1

                # mark current cell as rotton
                grid[xx][yy]=2

                # add to queue
                rottonQueue.append((xx,yy))

    return minutes_passed if fresh_count==0 else -1

print( orangesRotting(grid) )