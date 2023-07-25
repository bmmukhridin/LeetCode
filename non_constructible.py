# non-constructible

test = [5, 7, 1, 1, 2, 3, 22]

def nonContrasct(coins):
    coins.sort()
    print(coins)
    # print("\n")

    curentChange = 1

    for coin in coins:
        if coin > curentChange:
            return curentChange
        curentChange = curentChange + coin
        
    return curentChange
        

nonContrasct(test)




