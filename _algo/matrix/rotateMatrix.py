'''
    rotate 90 degree = transpose + flip horizontally
    https://www.geeksforgeeks.org/rotate-matrix-90-degree-without-using-extra-space-set-2/?ref=rp
'''

mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def rotateMatrix(mat):

    n = len(mat)

    for i in range(n):
        for j in range(i,n):
            tmp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = tmp

    for row in mat:
        print(row)


    print("after second rotation")

    for i in range(n):
        for j in range(n//2):
            tmp = mat[i][j]
            mat[i][j] = mat[i][n-j-1]
            mat[i][n-j-1] = tmp 

    for row in mat:
        print(row)


    return mat

print(rotateMatrix(mat))

# for row in mat:
#     print(row)
