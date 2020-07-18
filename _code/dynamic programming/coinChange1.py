
coins = [1,2,5]
amount = 11


def coinChange(coins, amount):
        if not amount: return 0
        min_coins = [0] + [float('inf')] * amount

        for c in coins:
            for i in range(c, amount + 1):
                print(c, i, min_coins, min_coins[i], min_coins[i-c])
                min_coins[i] = min(min_coins[i], min_coins[i - c] + 1)  # current val is min of current val or current val - coin + 1
                print(c, i, min_coins, min_coins[i], min_coins[i-c])
                print()

        return min_coins[-1] if min_coins[-1] != float('inf') else -1



def coinChange2(coins, amount):

        dp = [0] + [float('inf')]*amount

        for i in range(1, amount+1):
            for c in coins:
                    dp[i] = min( dp[i], dp[i-c]+1)


        print(dp)
        return dp[-1] if dp[-1]!=float('inf') else -1

        


print(coinChange2(coins, amount))