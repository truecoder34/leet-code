def maxProfit(prices) -> int:
    max_profit = 0

    current_min = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < current_min:
            current_min = prices[i]
        else:
            profit = prices[i] - current_min
            if profit > max_profit:
                max_profit = profit

    return max_profit


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))