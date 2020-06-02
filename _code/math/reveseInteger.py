import math

num = 1534236469

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

        # handle overflow
        if (rev > 2**31 / 10) or (rev == 2**31 / 10 and popped>7): return 0
        if (rev < -2**31 / 10) or (rev == -2**31 / 10 and popped<-8): return 0

        rev = rev * 10 + popped
    
        print(num, popped, rev)


    return rev*-1 if neg else rev

print( reverse(num) )
# print( reverse(123) )
# print( reverse(-123) )
# print( reverse(2**31) )
# print( reverse(-2**31) )