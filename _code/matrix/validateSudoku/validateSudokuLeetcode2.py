'''
    box method taken from:
    https://leetcode.com/problems/valid-sudoku/discuss/511365/Simple-Intuitive-Python-Approach

'''


bo = [
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




def validateBoard(bo):

    rows = [set() for i in range(9)]
    cols = [set() for i in range(9)]
    mMat = [set() for i in range(9)]

    for i in range(9):
        for j in range(9):
            cur = bo[i][j]

            if cur != '.':

                # validate row
                if cur not in rows:
                    rows[i].add(cur)
                else:
                    return False

                # validate col
                if cur not in cols:
                    cols[j].add(cur)
                else:
                    return False

                # validate box
                k = (i // 3 ) * 3 + j // 3

                if cur not in mMat[k]:
                    mMat[k].add(cur)
                else: return False

    return True






print(validateBoard(bo))