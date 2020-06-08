amount = 5
coins = [1,2,5]

def change(amount, coins):

    
    dp = [[1]+[0]*amount for _ in range(len(coins)+1)]
    for i in range(1, len(coins)+1):
        for j in range(1, amount+1):
            if coins[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    print(dp)

    return dp[len(coins)][amount]  # or dp[-1][-1]


print( change( amount, coins ) )