
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {coin: 0 for coin in coins}
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result[coin] += 1
    
    result = {coin: count for coin, count in result.items() if count > 0}
    return result

# Приклад використання
print(find_coins_greedy(113))