
mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def rotateMatrix(mat):

    N = len(mat)

    # transpose
    for i in range(N):
        for j in range(i, N):

            tmp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = tmp
    
    print( 'after transpose: ',  mat )

    # flip horizontally
    for i in range(N):
        for j in range(N//2):
            
            # swap j and N-j
            tmp = mat[i][j]
            mat[i][j] = mat[i][N-j-1]
            mat[i][N-j-1] = tmp
    
    print( 'after flip: ',  mat )


print(rotateMatrix(mat))
