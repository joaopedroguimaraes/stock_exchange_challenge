# Essa foi a primeira solução elaborada, de forma mais simples
#
# def highest_profit_on_stock_exchange(stock_values):
#     profit = 0
#     for i in range(0, len(stock_values) - 1):
#         for j in range(i, len(stock_values)):
#             actual_profit = stock_values[j] - stock_values[i]
#             if actual_profit > profit:
#                 profit = actual_profit
#     return profit


def lowest_value(array):
    position, value = 0, max(array)
    for i in range(0, len(array)):
        if array[i] < value:
            value = array[i]
            position = i
    return value, position


def highest_profit_on_stock_exchange(stock_values):
    lower, lower_pos = lowest_value(stock_values)
    return max(stock_values[lower_pos:]) - lower


if __name__ == '__main__':
    stock_values_per_day = [7, 1, 5, 3, 6, 4]
    # stock_values_per_day = [7,6,4,3,1]
    print(highest_profit_on_stock_exchange(stock_values_per_day))
