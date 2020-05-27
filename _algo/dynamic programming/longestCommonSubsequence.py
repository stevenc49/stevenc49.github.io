str1 = "AABA"
str2 = "AZB"

def lcs(text1, text2):

    n= len(text1)
    m= len(text2)

    # creates an [m+1][n+1] matrix, filled with zeros
    table=[[0]*(n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range (1, n+1):

            # first char is the same, so add 1 to count
            if text2[i-1]==text1[j-1]:
                table[i][j]= 1+table[i-1][j-1]
            # first char is different, so break into subproblems and take the max
            else:
                table[i][j]=max(table[i-1][j],table[i][j-1])

    
    print( [0]*(n+1) )
    print( range(m+1) )
    print( table )
    print( max(table) )    # this get the last element at the end of the list
    return max(max(table))  # this gets the last element at the bottom right corner (last element of both lists)



print( lcs(str1, str2))
