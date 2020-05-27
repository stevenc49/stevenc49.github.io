mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


def hasReachedTheEnd(m,n, curr_x, curr_y, dir):

    if dir==0: # right
        return True if curr_x==n else False

    elif dir==1: # down
        return False

    elif dir==2: # left
        return False
    else:
        return False

m = len(mat)        # vertical
n = len(mat[0])     # horizontal


curr_x, curr_y = 0, 0
dir = 0     # 0=right, 1=down, 2=left, 3=up



# go right
while curr_x < n:

    print(curr_y,curr_x, mat[curr_y][curr_x], dir)
    curr_x += 1


print(curr_y, curr_x)
while curr_y < m:
    print(curr_y,curr_x, mat[curr_y][curr_x], dir)
    curr_y += 1