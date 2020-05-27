nums = [3,0,1]

n = len(nums)

# xor index with value
xor = 0
for i, num in enumerate(nums):
    xor ^= i^num

# xor with length gives you missing num
missing = xor^n

print(missing)