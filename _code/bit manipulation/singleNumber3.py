
nums = [1,2,1,3,2,5]

def singleNumber(nums):
    
    xor = 0
    for n in nums:
        xor ^= n
        
    # xor = num1 ^ num2
    firstbit = xor & (xor-1) ^ xor
    num1 = 0
    for n in nums:
        if n & firstbit:
            num1 ^= n
            
    return [num1, num1^xor]

print( singleNumber(nums) )