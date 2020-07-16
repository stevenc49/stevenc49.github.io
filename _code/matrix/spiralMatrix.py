
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

def spiralMatrix(matrix):

    start_row = 0
    end_row = len(matrix)
    start_col = 0
    end_col = len(matrix)

    output = []
    while start_row<end_row or start_col<end_col:
        # right
        for i in range(start_col, end_col):
            output.append( matrix[start_row][i] )

        start_row+=1

        # down
        for i in range(start_row, end_row):
            output.append( matrix[i][end_col-1] )

        end_col-=1

        # left
        for i in range(end_col-1, start_col-1, -1):
            output.append( matrix[end_row-1][i] )

        end_row-=1

        # up
        for i in range(end_row-1, start_row-1, -1):
            output.append( matrix[i][start_col] )

        start_col+=1

    return output

print( spiralMatrix(matrix) )