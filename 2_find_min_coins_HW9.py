
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_count = [None] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_count[i] = coin

    result = {coin: 0 for coin in coins}
    while amount > 0:
        coin = coin_count[amount]
        result[coin] += 1
        amount -= coin
    
    result = {coin: count for coin, count in result.items() if count > 0}
    return result

# Приклад використання
print(find_min_coins(113))
print(find_min_coins(9))
