digits = [9]

def plusOne(digits):

    ptr = len(digits)-1
    carry = 1   # just set carry=1 to do get into the loop

    while carry==1:
        
        # edge case when carry=1 and ptr goes left off the edge (ie: '9')
        if ptr<0:
            digits.insert(0, 1)
            return digits

        # normal case: just add one to last digit
        if digits[ptr]>=0 and digits[ptr]<9:
            digits[ptr] = digits[ptr]+1
            carry=0
            return digits

        # edge case, set carry and move left
        elif digits[ptr]==9:
            digits[ptr] = 0
            carry = 1
            ptr-=1

    return digits

print( plusOne(digits) )