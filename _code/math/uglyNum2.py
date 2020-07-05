n=1690

def nthUglyNumber(n):
    
    uglyNums = [1]
    
    curr = 2
    while len(uglyNums)<n:
        
        print(curr)

        # factorize
        if curr%5==0 and int(curr/5) in uglyNums:
            uglyNums.append(curr)
        elif curr%3==0 and int(curr/3) in uglyNums:
            uglyNums.append(curr)
        elif curr%2==0 and int(curr/2) in uglyNums:
            uglyNums.append(curr)

        curr+=1
    

    return uglyNums[-1]

print(nthUglyNumber(n))