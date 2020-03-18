def how_many_coins(amount, coin_list):
    # Avoiding sorting to maintain O(n) time complexity
    num_coins = 0
    coin = max(coin_list)

    # until the change amount is created, iterate through coins from largest to smallest
    while amount != 0:
        if amount >= coin:
            possible_coins = int(amount / coin)  # round down number of coins that fit into amount
            amount = amount % coin
            num_coins += possible_coins
        coin_list.pop(coin_list.index(coin))
        if len(coin_list) == 0:
            return print(num_coins)
        coin = max(coin_list)
    return print(num_coins)
