import math

# digits = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]
digits = [7,2,8,5,0,9,1,2,9,5,3,6,6,7,3,2,8,4,3,7,9,5,7,7,4,7,4,9,4,7,0,1,1,1,7,4,0,0,6]

def plusOne(digits):
    num = 0
    exp = 0
    for i in reversed(range(len(digits))):
        print(num, i, exp, digits[i], pow(10, exp), math.floor( digits[i] * pow(10, exp)))
        num += math.floor( digits[i] * pow(10, exp))
        exp+=1
    

    plusOne = int(num+1)
    
    
    res = []
    while plusOne>0:
        
        pop = plusOne%10
        res = [pop] + res
        plusOne = plusOne//10
        
    return res


print(plusOne(digits))