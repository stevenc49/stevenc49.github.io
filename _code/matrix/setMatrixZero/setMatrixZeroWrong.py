mat = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]


def setZeroes(mat):

    if not mat: return None

    rows = len(mat)
    cols = len(mat[0])

    def zeroUpward(i,j):

        if i<0: return
        else:
            mat[i][j]=0
            zeroUpward(i-1,j)

    def zeroDownward(i,j):

        if i>=rows: return
        else:
            mat[i][j]=0
            zeroDownward(i+1,j)

    def zeroLeft(i,j):

        if j<0: return
        else:
            mat[i][j]=0
            zeroLeft(i,j-1)

    def zeroRight(i,j):

        if j>=cols: return
        else:
            mat[i][j]=0
            zeroRight(i,j+1)

    # go over mat first time to add cells to set (without modify matrix)
    for i in range(0, rows):
        for j in range(0, cols):
            if mat[i][j]==0:
                zeroUpward(i,j)
                zeroDownward(i,j)
                zeroLeft(i,j)
                zeroRight(i,j)

    return mat

setZeroes(mat)

print(mat)
