nums = [3,0,1]

n = len(nums)

# sum total if number wasn't missing
total = 0
for i in range(0, n+1):
    total = total + i


# sum actual numbers in array
arr_total = 0
for i in range(0, n):
    arr_total = arr_total + nums[i]

print(total)
print(arr_total)
print(total-arr_total)
