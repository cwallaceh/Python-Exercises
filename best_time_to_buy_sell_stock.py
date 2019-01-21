# Best Time to Buy and Sell Stock
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Example prices = [100, 180, 260, 310, 40, 535, 695]
# the maximum profit can earned by buying on day 0, selling on day 3.
# Again buy on day 4 and sell on day 6.
# If the given array of prices is sorted in decreasing order
# then profit cannot be earned at all.

# [[0, 80, 160, 210, -60, 435, 595]
#      [0, 80, 130, -140, 355, 515]
#           [0, 50, -220, 275, 435]
#               [0, -270, 225, 385]
#                     [0, 495, 655]
#                          [0, 160]
#                               [0]]

# prices = [100, 180, 260, 310, 40, 535, 695]


def best_time_to_buy_sell_I(prices):
    days = len(prices)
    buy = 0
    sell = 0
    max_profit = 0
    for i in range(days):
        for j in range(i, days):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
                buy = i + 1
                sell = j + 1
    return buy, sell, max_profit


# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time
#  (ie, you must sell the stock before you buy again).


def best_time_to_buy_sell_II(prices, n_transactions):
    """Dynamic Programming"""
    n_prices = len(prices)
    matrix = [[0] * n_prices for i in range(n_transactions + 1)]

    for i in range(1, n_transactions + 1):
        max_diff = -prices[0]
        for j in range(1, n_prices):
            matrix[i][j] = max(matrix[i][j - 1], prices[j] + max_diff)
            max_diff = max(max_diff, matrix[i - 1][j] - prices[j])
    return matrix


prices = [100, 180, 260, 310, 40, 535, 695]
buy, sell, max_profit = best_time_to_buy_sell_I(prices)
print("Buy on day: %s, Sell on day: %s, Profit: %s" % (buy, sell, max_profit))

prices = [100, 180, 260, 310, 40, 535, 695]
print(best_time_to_buy_sell_II(prices, 10))
