import math

n = 7

def numSquares(n):

    squares = [i**2 for i in range(0, int(math.sqrt(n))+1) ]
    dp = [float(inf)] * n

    print(squares)
    print(dp)

print( numSquares(n) )