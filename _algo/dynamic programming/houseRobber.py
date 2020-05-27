nums = [1,2,3,1]

# [1,2,3,1]
# [1,2,4,4]


def rob(nums):

    if not nums: return 0

    dp = [1] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        # dp.append( max( nums[i] + dp[i-2], dp[i-1] ) )
        dp[i] = max( nums[i] + dp[i-2], dp[i-1] )

    print(dp)

    return dp[-1]

print(rob(nums))