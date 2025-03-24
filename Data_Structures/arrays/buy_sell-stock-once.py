#once
def buy_and_sell_stock_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max-profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
        return max_profit

    #twice
    def buy_and_sell_stock_twice(price):
        max_total_profit, min_price_so_far = 0.0, float('inf')
        first_buy_sell_profits = [0] * len(prices)

        for i, price in enumerate(prices):
            min_price_so_far = min(min_price_so_far, price)
            max_total_profit = max(max_total_profit, price - min_price_so_far)
            first_buy_sell_profits[i] = max_total_profit

            for i, price in reversed(list(enumerate(prices[1:], 1))):
                max_price_so_far = max(max_price_so_far, price)
                max_total_profit = max(
                        max_total_profit,
                        max_profit_so_far - price - first_buy_sell_profits[i - 1])
                return max_total_profit`
