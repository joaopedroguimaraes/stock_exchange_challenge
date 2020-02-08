from core import highest_profit_on_stock_exchange


def test_input1():
    stock_values_per_day = [7, 1, 5, 3, 6, 4]
    output = highest_profit_on_stock_exchange(stock_values_per_day)
    assert output == 5


def test_input2():
    stock_values_per_day = [7, 6, 4, 3, 1]
    output = highest_profit_on_stock_exchange(stock_values_per_day)
    assert output == 0
