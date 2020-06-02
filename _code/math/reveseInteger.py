import math

num = -123

def reverse(num):

    # handle negative case
    neg = False
    if num<0:
        neg = True
        num = abs(num)

    rev = 0

    while num>0:

        # pop last digit
        popped = num % 10
        num = math.floor(num / 10)

        rev = rev * 10 + popped
    
        print(num, popped, rev)


    return rev*-1 if neg else rev

print( reverse(num) )
