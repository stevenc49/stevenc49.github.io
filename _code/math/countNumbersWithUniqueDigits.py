'''

    https://leetcode.com/problems/count-numbers-with-unique-digits/

'''

# from math import *
import math


def isUniqueInteger(n):

    mymap = dict()

    while(n>0):
        digit=n%10
        #print(digit)
        
        if not digit in mymap:
            mymap[digit] = 1
        else:
            return False

        n=n//10

        #print(mymap)
    
    return True


def countNumbersWithUniqueDigits(n):

    count = 0

    for i in range(0, pow(10, n)):
        if isUniqueInteger(i):
            count = count + 1
    
    return count


def main():

    # countNumbersWithUniqueDigits(None, 2)
    print( countNumbersWithUniqueDigits(2) )
    


if __name__ == "__main__":
    main()