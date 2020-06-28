import math

n = 7

def numSquares(n):

    squares = [i**2 for i in range(0, math.sqrt(n))]

    print(squares)

print( numSquares(n) )