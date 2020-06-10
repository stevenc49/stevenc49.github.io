'''
    box method taken from:
    https://leetcode.com/problems/valid-sudoku/discuss/511365/Simple-Intuitive-Python-Approach

'''

boValid = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

boInvalid = [
  ["5","3",".",".","7",".",".",".","."],
  ["6","8",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]




def validateBoard(bo):

    # validate row
    for row in range(len(bo)):
        row_set = {}
        for col in range(len(bo[row])):
            
            val = bo[row][col]
            if val != ".":
                if val not in row_set:
                    row_set[ val ] =  1
                else:
                    print(val + " is duplicated in row")
                    return False

    

    # validate col
    for col in range(len(bo[0])):

        col_set = {}
        for row in range(len(bo)):

            val = bo[row][col]

            if val != ".":

                if val not in col_set:
                    col_set[val] = 1
                else:
                    print(val + " is duplicated in col")
                    return False


    # validate box
    mMat = [set() for i in range(9)]
    print( mMat )

    for i in range(9):
        for j in range(9):
            cur = bo[i][j]
            # print(i,j,cur)
            if cur != '.':

                k = (i // 3 ) * 3 + j // 3

                print(i,j,cur, k, mMat)

                if cur not in mMat[k]:
                    mMat[k].add(cur)
                else: return False

    return True






bo = boInvalid
print(validateBoard(bo))