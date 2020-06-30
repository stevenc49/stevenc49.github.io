board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

def exist(board, word):

    R = len(board)
    C = len(board[0])

    def exist(i, j, word, index):

      # found word
      if index==len(word):
        return True

      # boundary checks or next letter is not right (backtrack)
      if i<0 or i>=R or j<0 or j>=C or board[i][j]!=word[index]:
        return False

      

print( exist(board, "ABC") )
