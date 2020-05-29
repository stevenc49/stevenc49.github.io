mat = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]


def setZeroes(mat):

    if not mat: return None

    R = len(mat)
    C = len(mat[0])

    zero_rows = set()
    zero_cols = set()

    # iterate over matrix once to add row and column that needs to be zeroed (without modifying it in place yet)
    for i in range(0, R):
        for j in range(0, C):
            if mat[i][j]==0:
                zero_rows.add(i)
                zero_cols.add(j)
    
    # go over second time to actually zero out rows and columns
    for i in range(0, R):
        for j in range(0, C):
            if i in zero_rows:
                mat[i][j]=0
            if j in zero_cols:
                mat[i][j]=0


setZeroes(mat)

print(mat)
