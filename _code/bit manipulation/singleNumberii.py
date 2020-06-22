nums = [2,2,3,2]

def singleNumber(nums):
    single = 0
    for i in range(32):
        count = 0
        for num in nums:
            # if num & (1<<i) == (1<<i): count +=1
            if num & (1<<i) == (1<<i): count += 1
            
        single |= (count%3) << 1
        
    return single if single < (1<<31) else sing
    le - (1<<32)

# def singleNumber(nums):
#     single = 0
#     for i in range(32):
#         count = 0
#         for num in nums:
#             if num & (1<<i) == (1<<i): count += 1
#         single |= (count%3) << i
        
#     return single if single < (1<<31) else single - (1<<32) 

print(singleNumber(nums))