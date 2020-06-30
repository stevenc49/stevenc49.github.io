board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

def exist(board, word):

    R = len(board)
    C = len(board[0])

    def searchWord(i, j, word, index):

      if index==len(word):
        return True

      if i<0 or i>=R or j<0 or j>=C or board[i][j]!=word[index]:
        return False

      tmp = board[i][j]
      board[i][j] = ' '
      # found = searchWord(i+1,j,word,index+1)
      found = searchWord(i-1,j,word,index+1) or \
        searchWord(i+1,j,word,index+1) or \
        searchWord(i,j-1,word,index+1) or \
        searchWord(i,j+1,word,index + 1)

      board[i][j] = tmp
      return found

    for i in range(R):
      for j in range(C):
        if board[i][j]==word[0] and searchWord(i,j,word,0):
          return True

    return False

print( exist(board, "ABC") )
