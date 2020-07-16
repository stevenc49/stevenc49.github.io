
matrix1 = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

matrix2 = [
  [1, 2, 3, 4],
  [4,5,6,7],
  [7,8,9,10]
]

matrix3 = [
    [2,5,8],[4,0,-1]
]

def spiralMatrix1(matrix):

    if not matrix: return []

    start_row = 0
    end_row = len(matrix)
    start_col = 0
    end_col = len(matrix[0])

    output = []
    while start_row<end_row and start_col<end_col:  
        # right
        for i in range(start_col, end_col):
            output.append( matrix[start_row][i] )

        start_row+=1

        # down
        for i in range(start_row, end_row):
            output.append( matrix[i][end_col-1] )


        end_col-=1

        if end_row <= start_row: break  # handles edge case with matrix2

        # left
        for i in range(end_col-1, start_col-1, -1):
            output.append( matrix[end_row-1][i] )

        end_row-=1

        if end_col <= start_col: break  # handles edge case with matrix2

        # up
        for i in range(end_row-1, start_row-1, -1):
            output.append( matrix[i][start_col] )

        start_col+=1

    return output




print( spiralMatrix1(matrix3) )