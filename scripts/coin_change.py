def how_many_coins(amount, coin_list):
    # amount = the change amount to make
    # coin_list = list of coins provided
    # sort it in descending order
    coin_list.sort(reverse=True)
    num_coins = 0

    # until the change amount is created, iterate through coins from largest to smallest
    while amount != 0:
        for coin in coin_list:
            if amount >= coin:
                possible_coins = int(amount / coin) # round down number of coins that fit into amount
                amount = amount % coin
                num_coins += possible_coins
    return num_coins
